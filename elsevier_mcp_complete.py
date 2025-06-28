#!/usr/bin/env python3
"""
Elsevier MCP Complete Server
Cursorで使用するすべてのMCPツール機能を実装
"""

import asyncio
import json
import sys
import requests
import os
from datetime import datetime

# Elsevier API設定
API_KEY = os.getenv("ELSEVIER_API_KEY")
if not API_KEY:
    print("❌ Error: ELSEVIER_API_KEY environment variable is not set", file=sys.stderr)
    print("Please set your API key: export ELSEVIER_API_KEY='your_api_key_here'", file=sys.stderr)
    sys.exit(1)

BASE_URL = "https://api.elsevier.com"
HEADERS = {"X-ELS-APIKey": API_KEY, "Accept": "application/json"}

class ElsevierMCPServer:
    def __init__(self):
        self.tools = self._define_tools()

    def _define_tools(self):
        """全ツール定義（MCPプロトコル準拠）"""
        return {
            "search_papers": {
                "name": "search_papers",
                "description": "Scopus論文データベースから論文を検索します。キーワード、著者名、年度等で検索可能。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "検索キーワード（例: 'machine learning', '著者名', '分野名'）"
                        },
                        "count": {
                            "type": "integer",
                            "description": "取得件数（最大25）",
                            "minimum": 1,
                            "maximum": 25
                        },
                        "year": {
                            "type": "string",
                            "description": "発行年（YYYY形式）"
                        }
                    },
                    "required": ["query"]
                }
            },
            "get_paper_abstract": {
                "name": "get_paper_abstract",
                "description": "論文のEIDまたはDOIから詳細な抄録とメタデータを取得します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "eid": {
                            "type": "string",
                            "description": "論文のElsevier ID（EID）"
                        },
                        "doi": {
                            "type": "string",
                            "description": "論文のDigital Object Identifier（DOI）"
                        }
                    }
                }
            },
            "get_author_info": {
                "name": "get_author_info",
                "description": "著者IDから研究者の詳細プロファイルを取得します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "author_id": {
                            "type": "string",
                            "description": "Scopus著者ID"
                        }
                    },
                    "required": ["author_id"]
                }
            },
            "analyze_research_trends": {
                "name": "analyze_research_trends",
                "description": "指定された研究分野の年別論文数推移を分析します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "研究分野キーワード（例: 'artificial intelligence', 'quantum computing'）"
                        },
                        "years": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "分析対象年のリスト（例: [2022, 2023, 2024]）"
                        }
                    },
                    "required": ["field"]
                }
            },
            "get_institution_papers": {
                "name": "get_institution_papers",
                "description": "指定された機関の論文統計と最新論文リストを取得します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "institution": {
                            "type": "string",
                            "description": "機関名（例: 'MIT', 'Stanford University'）"
                        },
                        "year": {
                            "type": "integer",
                            "description": "対象年"
                        }
                    },
                    "required": ["institution"]
                }
            },
            "search_open_access_papers": {
                "name": "search_open_access_papers",
                "description": "指定された分野のオープンアクセス論文を検索します。",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "field": {
                            "type": "string",
                            "description": "研究分野（例: 'machine learning', 'climate change'）"
                        },
                        "count": {
                            "type": "integer",
                            "description": "取得件数",
                            "minimum": 1,
                            "maximum": 20
                        }
                    },
                    "required": ["field"]
                }
            }
        }

    async def search_papers(self, arguments: dict) -> dict:
        """論文検索"""
        query = arguments.get("query", "")
        count = arguments.get("count", 10)
        year = arguments.get("year", "")

        # クエリ構築
        search_query = f"TITLE-ABS-KEY({query})"
        if year:
            search_query += f" AND PUBYEAR = {year}"

        url = f"{BASE_URL}/content/search/scopus"
        params = {
            "query": search_query,
            "count": min(count, 25),
            "sort": "citedby-count"
        }

        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=15)
            if response.ok:
                data = response.json()
                entries = data.get('search-results', {}).get('entry', [])
                total = data.get('search-results', {}).get('opensearch:totalResults', 0)

                results = []
                for entry in entries:
                    paper = {
                        "title": entry.get('dc:title', 'No title'),
                        "authors": entry.get('dc:creator', 'Unknown'),
                        "journal": entry.get('prism:publicationName', 'Unknown'),
                        "year": entry.get('prism:coverDate', ''),
                        "citations": int(entry.get('citedby-count', 0)),
                        "doi": entry.get('prism:doi', ''),
                        "eid": entry.get('eid', '')
                    }
                    results.append(paper)

                return {
                    "success": True,
                    "total_results": int(total),
                    "papers": results,
                    "query": query
                }
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def get_paper_abstract(self, arguments: dict) -> dict:
        """論文抄録取得"""
        eid = arguments.get("eid", "")
        doi = arguments.get("doi", "")

        if not eid and not doi:
            return {"success": False, "error": "EIDまたはDOIが必要です"}

        # EID優先
        if eid:
            url = f"{BASE_URL}/content/abstract/eid/{eid}"
        else:
            url = f"{BASE_URL}/content/abstract/doi/{doi}"

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.ok:
                data = response.json()
                abstract_response = data.get('abstracts-retrieval-response', {})
                coredata = abstract_response.get('coredata', {})

                result = {
                    "title": coredata.get('dc:title', 'No title'),
                    "abstract": coredata.get('dc:description', 'No abstract'),
                    "authors": coredata.get('dc:creator', 'Unknown'),
                    "journal": coredata.get('prism:publicationName', 'Unknown'),
                    "year": coredata.get('prism:coverDate', ''),
                    "doi": coredata.get('prism:doi', ''),
                    "eid": coredata.get('eid', ''),
                    "citations": coredata.get('citedby-count', '0')
                }

                return {"success": True, "paper": result}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def get_author_info(self, arguments: dict) -> dict:
        """著者情報取得"""
        author_id = arguments.get("author_id", "")

        if not author_id:
            return {"success": False, "error": "author_idが必要です"}

        url = f"{BASE_URL}/analytics/scival/author/{author_id}"

        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.ok:
                data = response.json()
                author_data = data.get('author', {})

                result = {
                    "author_id": author_id,
                    "name": author_data.get('name', 'Unknown'),
                    "current_institution": author_data.get('currentInstitutionName', 'Unknown'),
                    "scopus_url": author_data.get('link', {}).get('@href', '')
                }

                return {"success": True, "author": result}
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def analyze_research_trends(self, arguments: dict) -> dict:
        """研究分野トレンド分析"""
        field = arguments.get("field", "")
        years = arguments.get("years", [2022, 2023, 2024])

        if not field:
            return {"success": False, "error": "research fieldが必要です"}

        url = f"{BASE_URL}/content/search/scopus"
        yearly_data = {}

        try:
            for year in years:
                params = {
                    "query": f"TITLE-ABS-KEY({field}) AND PUBYEAR = {year}",
                    "count": 1
                }

                response = requests.get(url, headers=HEADERS, params=params, timeout=10)
                if response.ok:
                    data = response.json()
                    total = int(data.get('search-results', {}).get('opensearch:totalResults', 0))
                    yearly_data[year] = total

            # 成長率計算
            growth_rates = {}
            years_sorted = sorted(yearly_data.keys())
            for i in range(1, len(years_sorted)):
                prev_year = years_sorted[i-1]
                curr_year = years_sorted[i]
                if yearly_data[prev_year] > 0:
                    growth_rate = ((yearly_data[curr_year] - yearly_data[prev_year]) / yearly_data[prev_year]) * 100
                    growth_rates[f"{prev_year}-{curr_year}"] = round(growth_rate, 2)

            return {
                "success": True,
                "field": field,
                "yearly_papers": yearly_data,
                "growth_rates": growth_rates,
                "total_papers": sum(yearly_data.values())
            }

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def get_institution_papers(self, arguments: dict) -> dict:
        """機関論文統計"""
        institution = arguments.get("institution", "")
        year = arguments.get("year", 2024)

        if not institution:
            return {"success": False, "error": "institution nameが必要です"}

        url = f"{BASE_URL}/content/search/scopus"
        params = {
            "query": f"aff({institution}) AND PUBYEAR = {year}",
            "count": 5,
            "sort": "citedby-count"
        }

        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=15)
            if response.ok:
                data = response.json()
                entries = data.get('search-results', {}).get('entry', [])
                total = int(data.get('search-results', {}).get('opensearch:totalResults', 0))

                top_papers = []
                for entry in entries:
                    paper = {
                        "title": entry.get('dc:title', 'No title'),
                        "authors": entry.get('dc:creator', 'Unknown'),
                        "journal": entry.get('prism:publicationName', 'Unknown'),
                        "citations": int(entry.get('citedby-count', 0)),
                        "doi": entry.get('prism:doi', '')
                    }
                    top_papers.append(paper)

                return {
                    "success": True,
                    "institution": institution,
                    "year": year,
                    "total_papers": total,
                    "top_papers": top_papers
                }
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}

        except Exception as e:
            return {"success": False, "error": str(e)}

    async def search_open_access_papers(self, arguments: dict) -> dict:
        """オープンアクセス論文検索"""
        field = arguments.get("field", "")
        count = arguments.get("count", 10)

        if not field:
            return {"success": False, "error": "research fieldが必要です"}

        url = f"{BASE_URL}/content/search/scopus"
        params = {
            "query": f"TITLE-ABS-KEY({field}) AND OPENACCESS(1) AND PUBYEAR = 2024",
            "count": min(count, 20),
            "sort": "citedby-count"
        }

        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=15)
            if response.ok:
                data = response.json()
                entries = data.get('search-results', {}).get('entry', [])
                total = int(data.get('search-results', {}).get('opensearch:totalResults', 0))

                papers = []
                for entry in entries:
                    paper = {
                        "title": entry.get('dc:title', 'No title'),
                        "authors": entry.get('dc:creator', 'Unknown'),
                        "journal": entry.get('prism:publicationName', 'Unknown'),
                        "citations": int(entry.get('citedby-count', 0)),
                        "doi": entry.get('prism:doi', ''),
                        "open_access": True
                    }
                    papers.append(paper)

                return {
                    "success": True,
                    "field": field,
                    "total_open_access": total,
                    "papers": papers
                }
            else:
                return {"success": False, "error": f"API Error: {response.status_code}"}

        except Exception as e:
            return {"success": False, "error": str(e)}

async def handle_request(server, request):
    """MCPリクエスト処理"""
    method = request.get("method")

    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "resources": {}
                },
                "serverInfo": {
                    "name": "elsevier-mcp-complete-server",
                    "version": "1.0.0"
                }
            }
        }

    elif method == "tools/list":
        tools_list = []
        for tool_name, tool_def in server.tools.items():
            tools_list.append({
                "name": tool_def["name"],
                "description": tool_def["description"],
                "inputSchema": tool_def["inputSchema"]
            })

        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "result": {"tools": tools_list}
        }

    elif method == "tools/call":
        tool_name = request.get("params", {}).get("name")
        arguments = request.get("params", {}).get("arguments", {})

        if tool_name in server.tools:
            # ツール実行
            handler = getattr(server, tool_name)
            result = await handler(arguments)

            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(result, ensure_ascii=False, indent=2)
                    }]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {"code": -32601, "message": f"Tool not found: {tool_name}"}
            }

    else:
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {"code": -32601, "message": f"Method not found: {method}"}
        }

async def main():
    """メイン処理"""
    server = ElsevierMCPServer()
    print("Elsevier MCP Complete Server started", file=sys.stderr)

    # stdio での通信処理
    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break

            request = json.loads(line.strip())
            response = await handle_request(server, request)

            print(json.dumps(response), flush=True)

        except EOFError:
            break
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id") if 'request' in locals() else None,
                "error": {"code": -32603, "message": str(e)}
            }
            print(json.dumps(error_response), flush=True)

if __name__ == "__main__":
    asyncio.run(main())