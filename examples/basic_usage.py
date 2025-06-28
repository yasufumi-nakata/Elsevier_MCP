#!/usr/bin/env python3
"""
Elsevier MCP Serverの基本的な使用例

このスクリプトはElsevier MCP Serverの主要機能を実演します。
使用前にELSEVIER_API_KEY環境変数を設定してください。
"""

import json
import os
import sys

# MCPサーバーファイルのパスを追加
sys.path.append('..')

def check_env():
    """環境変数をチェック"""
    api_key = os.getenv('ELSEVIER_API_KEY')
    if not api_key:
        print("❌ ELSEVIER_API_KEY環境変数が設定されていません")
        print("以下のコマンドで設定してください:")
        print("export ELSEVIER_API_KEY='your_api_key_here'")
        return False
    print(f"✅ APIキーが設定されています: {api_key[:10]}...")
    return True

def demo_paper_search():
    """論文検索のデモ"""
    print("\n🔍 論文検索デモ")
    print("=" * 50)

    try:
        # MCPサーバーのインポート
        try:
            from elsevier_mcp_complete import search_papers  # type: ignore
        except ImportError:
            print("❌ elsevier_mcp_complete モジュールが見つかりません")
            print("上位ディレクトリに移動して実行してください")
            return False

        # AI関連論文を検索
        result = search_papers("artificial intelligence", 3)
        print(f"検索結果: {len(result.get('entries', []))}件の論文を発見")

        for i, paper in enumerate(result.get('entries', [])[:3], 1):
            print(f"\n{i}. {paper.get('dc:title', 'タイトル不明')}")
            print(f"   著者: {paper.get('dc:creator', '著者不明')}")
            print(f"   発行年: {paper.get('prism:coverDate', '年不明')}")
            print(f"   引用数: {paper.get('citedby-count', '0')}")

        return True
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def demo_author_info():
    """著者情報取得のデモ"""
    print("\n👨‍🔬 著者情報取得デモ")
    print("=" * 50)

    try:
        from elsevier_mcp_complete import get_author_info

        # 著者IDの例（Ahmed, Jabed Foyez）
        author_id = "57817454300"
        result = get_author_info(author_id)

        if 'author-retrieval-response' in result:
            author = result['author-retrieval-response'][0]
            profile = author.get('coredata', {})

            print(f"名前: {profile.get('indexed-name', '不明')}")
            print(f"所属: {profile.get('current-affiliation', '不明')}")
            print(f"論文数: {author.get('coredata', {}).get('document-count', '不明')}")
            print(f"被引用数: {author.get('coredata', {}).get('cited-by-count', '不明')}")

        return True
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def demo_research_trends():
    """研究トレンド分析のデモ"""
    print("\n📊 研究トレンド分析デモ")
    print("=" * 50)

    try:
        from elsevier_mcp_complete import analyze_research_trends

        # 機械学習分野の年別推移
        result = analyze_research_trends("machine learning", [2022, 2023, 2024])

        print("機械学習分野の年別論文数推移:")
        for year_data in result.get('trends', []):
            year = year_data.get('year')
            count = year_data.get('count', 0)
            print(f"  {year}年: {count:,}件")

        return True
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def demo_open_access():
    """オープンアクセス論文検索のデモ"""
    print("\n🔓 オープンアクセス論文検索デモ")
    print("=" * 50)

    try:
        from elsevier_mcp_complete import search_open_access_papers

        result = search_open_access_papers("quantum computing", 3)

        print(f"オープンアクセス論文: {len(result.get('entries', []))}件発見")
        for i, paper in enumerate(result.get('entries', [])[:3], 1):
            print(f"\n{i}. {paper.get('dc:title', 'タイトル不明')}")
            print(f"   アクセス: 🔓 オープンアクセス")
            print(f"   DOI: {paper.get('prism:doi', 'DOI不明')}")

        return True
    except Exception as e:
        print(f"❌ エラー: {e}")
        return False

def main():
    """メイン実行関数"""
    print("🔬 Elsevier MCP Server - 基本使用例")
    print("=" * 60)

    # 環境変数チェック
    if not check_env():
        return 1

    # 各デモを実行
    demos = [
        ("論文検索", demo_paper_search),
        ("著者情報取得", demo_author_info),
        ("研究トレンド分析", demo_research_trends),
        ("オープンアクセス論文検索", demo_open_access),
    ]

    success_count = 0
    for name, demo_func in demos:
        try:
            if demo_func():
                success_count += 1
        except Exception as e:
            print(f"❌ {name}でエラーが発生: {e}")

    # 結果サマリー
    print(f"\n📋 実行結果: {success_count}/{len(demos)} 件のデモが成功")

    if success_count == len(demos):
        print("✅ すべてのデモが正常に動作しました！")
        return 0
    else:
        print("⚠️  一部のデモで問題が発生しました。APIキーや接続を確認してください。")
        return 1

if __name__ == "__main__":
    exit(main())