# Elsevier MCP Server

ElsevierのScopus APIを活用したMCP (Model Context Protocol) サーバーです。Cursor IDE のAI Composerから直接学術論文の検索・分析・研究者情報取得が可能になります。

🌐 **リンク**：https://github.com/yasufumi-nakata/elsevier-mcp-server
📖 **English README**: [README.md](README.md)

## 📚 概要

このプロジェクトは、世界最大級の学術データベースであるElsevierのAPIサービスをMCP (Model Context Protocol) プロトコル経由で提供します。MCPは、AI アプリケーションと外部データソースを標準化して接続するためのプロトコルで、「AI界のUSB-C」とも呼ばれています。

### 🔗 利用可能なElsevier APIサービス

- **Scopus API**: 世界最大級の引用・抄録データベース（7,800万件の記録、1,600万著者プロファイル）
- **Abstract Retrieval API**: 論文の詳細抄録とメタデータ取得
- **SciVal API**: 研究パフォーマンス分析と著者メトリクス

### ⚠️ 重要：API・AI利用規約について

**必読**: 利用前にElsevierのポリシーを必ずお読みください：

- **📋 API利用規約**: すべての使用は[Elsevier API Service Agreement](https://dev.elsevier.com/api_service_agreement.html)に準拠する必要があります
- **🤖 AI利用ポリシー**: 本ツールで取得したデータは[ElsevierのAIガイドライン](https://www.elsevier.com/about/policies/ai-policy)に従ってください
- **📊 テキスト・データマイニング**: 学術的なテキストマイニングは[TDMポリシー](https://www.elsevier.com/about/open-science/research-data/text-and-data-mining)に準拠してください
- **🚫 禁止事項**:
  - 明示的な許可なしでのAIモデル訓練への使用
  - 研究目的を超えた大規模データ収集
  - 取得データの商用再配布
- **🔒 データ保持**: 適切なライセンスなしに取得データを永続的に保存することは禁止されています

詳細な規約については[Elsevier Developer Portal](https://dev.elsevier.com/)をご確認ください。

## ✨ 主な機能

### 🔍 論文検索
- キーワード、著者名、分野での論文検索
- 年度指定検索
- 最大25件の検索結果取得

### 👨‍🔬 研究者分析
- 著者プロファイルの詳細情報
- ORCID IDによる研究者検索
- 被引用数、H-Index、研究活動指標

### 📊 研究トレンド分析
- 分野別年度推移分析
- 機関別論文統計
- オープンアクセス論文検索

### 📄 論文詳細情報
- 抄録とメタデータ取得
- DOIおよびEIDによる詳細検索

## 🚀 クイックスタート

### ステップ1: 必要な環境を確認

以下の環境が必要です：
- 🐍 **Python 3.7以上** (Python 3.10以上を推奨)
- 💻 **Cursor IDE** (最新版を使用してください)
- 🔑 **Elsevier API Key** (Elsevier Developer Portalから取得)

### ステップ2: プロジェクトをダウンロード

```bash
# GitHubからプロジェクトをクローン
git clone https://github.com/yasufumi-nakata/elsevier-mcp-server.git
cd elsevier-mcp-server

# 必要なPythonライブラリをインストール
pip install -r requirements.txt
```

### ステップ3: Elsevier API Keyを取得

#### 3-1. Elsevier Developer Portalでアカウント作成

1. [Elsevier Developer Portal](https://dev.elsevier.com/)にアクセス
2. 「I want an API Key」をクリック
3. アカウント情報を入力してアカウント作成

#### 3-2. APIキーを生成

1. ログイン後、「My API Key」を選択
2. 新しいAPIキーを作成
3. **Elsevierの現行利用規約・ポリシーに従ってください**

#### 3-3. 環境変数を設定

**Windows (コマンドプロンプト):**
```cmd
set ELSEVIER_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:ELSEVIER_API_KEY="your_api_key_here"
```

**macOS/Linux:**
```bash
export ELSEVIER_API_KEY="your_api_key_here"
```

### ステップ4: Cursor IDEでMCPを設定

#### 4-1. Cursor設定を開く

1. **Cursor IDE**を起動
2. `⌘ + ,` (Mac) または `Ctrl + ,` (Windows/Linux) で設定を開く
3. 左側のメニューから「**MCP**」を選択

#### 4-2. MCP サーバーを追加

1. 「**Add new global MCP server**」ボタンをクリック
2. 以下のJSON設定を追加：

```json
{
  "mcpServers": {
    "elsevier-research": {
      "comment": "🔬 Elsevier学術論文検索MCP",
      "command": "python3",
      "args": ["/フルパス/to/elsevier_mcp_complete.py"],
      "env": {
        "ELSEVIER_API_KEY": "ここにあなたのAPIキーを入力"
      }
    }
  }
}
```

**重要**:
- `/フルパス/to/elsevier_mcp_complete.py` を実際のファイルパスに置き換えてください
- `ここにあなたのAPIキーを入力` を取得したAPIキーに置き換えてください

#### 4-3. 設定を保存して確認

1. 設定ファイルを保存 (`⌘ + S` または `Ctrl + S`)
2. MCPサーバーリストに緑色のマークが表示されれば成功です
3. エラーが表示される場合は、ファイルパスやAPIキーを再確認してください

## 📖 使用方法

### ステップ1: Cursor AI Composerを開く

1. **Cursor IDE**で新しいチャットを開始
2. **右上の「Composer」アイコン**をクリック、または `⌘ + I` (Mac) / `Ctrl + I` (Windows)
3. **「Agent」モード**に設定されていることを確認（MCPツールを使用するために必要）

### ステップ2: 論文検索を試してみる

以下のような質問を入力してみてください：

#### 🔍 基本的な論文検索
```
「機械学習に関する論文を5件検索してください」
```

#### 📊 研究トレンド分析
```
「2023年のAIと機械学習分野の研究動向を分析してください」
```

#### 👨‍🔬 研究者情報の取得
```
「ORCID: 0000-0003-1419-2405 の研究者について詳しく教えてください」
```

#### 🏛️ 機関別の研究状況
```
「MIT（マサチューセッツ工科大学）の2023年の論文数と主要な研究分野を調べてください」
```

#### 🔓 オープンアクセス論文の検索
```
「quantum computingのオープンアクセス論文を3件検索してください」
```

### ステップ3: ツールの承認と実行

1. AIが**「Tool Approval Required」**と表示したら、「**Use Tool**」をクリック
2. 結果が表示されるまで数秒お待ちください
3. **詳細情報が必要な場合**は、追加の質問を続けて入力できます

### 💡 使用のコツ

- **具体的なキーワード**を使用すると、より正確な結果が得られます
- **年度を指定**すると、最新の研究動向を把握できます
- **論文数を指定**して、必要な情報量を調整できます

## 🛠️ 利用可能なツール

| ツール名 | 説明 | パラメータ |
|---------|------|-----------|
| `search_papers` | 論文検索 | `query`, `count`, `year` |
| `get_paper_abstract` | 論文抄録取得 | `eid` または `doi` |
| `get_author_info` | 著者情報取得 | `author_id` |
| `analyze_research_trends` | 研究トレンド分析 | `field`, `years` |
| `get_institution_papers` | 機関別論文統計 | `institution`, `year` |
| `search_open_access_papers` | オープンアクセス論文検索 | `field`, `count` |

## 🧪 テスト

```bash
# APIテストの実行
python test.py

# 個別機能テスト
python -c "
import json
from elsevier_mcp_complete import search_papers
result = search_papers('artificial intelligence', 3)
print(json.dumps(result, indent=2, ensure_ascii=False))
"
```

## 🔧 トラブルシューティング

### 🚨 よくある問題と解決方法

#### 問題1: 「MCPサーバーが起動しない」

**症状**: Cursor設定でMCPサーバーに赤いマークが表示される

**解決方法**:
1. **ファイルパスを確認**:
   ```bash
   # ファイルの場所を確認
   ls -la /your/path/to/elsevier_mcp_complete.py
   ```
2. **Python実行権限を確認**:
   ```bash
   # ファイルに実行権限を付与
   chmod +x elsevier_mcp_complete.py
   ```
3. **必要なライブラリを再インストール**:
   ```bash
   pip install -r requirements.txt
   ```

#### 問題2: 「APIキーエラーが発生する」

**症状**: `401 Unauthorized` エラー、「Invalid API Key」、または「ELSEVIER_API_KEY environment variable is not set」

**解決方法**:
1. **「environment variable is not set」でサーバーが終了する場合**: APIキーが見つからない場合、MCPサーバーは自動的に終了します
   - APIキーを設定: `export ELSEVIER_API_KEY="your_api_key_here"`
   - CursorでMCPサーバーを再起動
2. **APIキーの形式を確認**: 32文字の英数字であることを確認
3. **環境変数を再設定**:
   ```bash
   # 現在の設定を確認
   echo $ELSEVIER_API_KEY

   # 再設定
   export ELSEVIER_API_KEY="your_actual_api_key"
   ```
4. **Cursor設定を再読み込み**: 設定を保存してCursorを再起動

#### 問題3: 「検索結果が表示されない」

**症状**: 「論文が見つかりませんでした」と表示される

**解決方法**:
1. **キーワードを変更**: より一般的な用語を試す（例：「AI」→「artificial intelligence」）
2. **年度制限を外す**: 特定の年度指定を削除
3. **オープンアクセス検索を試す**: 無料でアクセス可能な論文のみを検索

#### 問題4: 「Cursor Agentモードでツールが使用されない」

**症状**: 通常の回答のみが返され、MCP ツールが使用されない

**解決方法**:
1. **Agent モードを確認**: Chat設定が「Agent」になっていることを確認
2. **明示的にツール使用を指示**:
   ```
   「search_papersツールを使って機械学習の論文を検索してください」
   ```
3. **Auto-run を有効化**: Cursor 設定でツールの自動実行を有効にする

#### 問題5: 「使用制限に達している」

**症状**: `Rate limit exceeded` エラー

**解決方法**:
- **使用制限**: Elsevier Developer Portalで現在のAPI制限を確認してください
- **制限リセット**: 毎週月曜日に制限がリセットされます
- **制限拡張**: 必要に応じてElsevierに拡張アクセスについて問い合わせてください

### 📞 サポートが必要な場合

1. **GitHub Issues**: [問題を報告](https://github.com/yasufumi-nakata/elsevier-mcp-server/issues)
2. **Elsevier API サポート**: apisupport@elsevier.com
3. **Cursor サポート**: [Cursor ヘルプセンター](https://docs.cursor.com/)

### ✅ 動作確認チェックリスト

設定が正しく動作しているかを確認するために：

- [ ] Python 3.7+ がインストールされている
- [ ] 必要なライブラリがインストールされている
- [ ] Elsevier API キーが有効
- [ ] CursorのMCP設定でサーバーが緑色
- [ ] Agent モードが選択されている
- [ ] ファイルパスが正確に設定されている

## 📦 依存関係

- `requests`: HTTP APIクライアント
- `python-dotenv`: 環境変数管理

詳細は `requirements.txt` を参照してください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 🤝 コントリビューション

プルリクエストやイシューの報告を歓迎します！

1. フォークしてください
2. フィーチャーブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを開いてください

## 🔗 関連リンク

### 📚 公式ドキュメント
- [Elsevier Developer Portal](https://dev.elsevier.com/) - APIキー取得と仕様書
- [Scopus API Documentation](https://dev.elsevier.com/documentation/ScopusSearchAPI.wadl) - Scopus API の詳細仕様
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) - MCP プロトコルの公式サイト
- [Cursor MCP Documentation](https://docs.cursor.com/context/model-context-protocol) - Cursor での MCP 設定方法

### 🛠️ 開発ツール
- [Cursor IDE](https://cursor.sh/) - AI 統合開発環境
- [MCP Directory](https://cursor.directory/mcp) - 1800+ MCP サーバーの一覧
- [GitHub - MCP Servers](https://github.com/modelcontextprotocol/servers) - 公式MCPサーバーコレクション

### 🎓 学習リソース
- [MCP Tutorial Series](https://medium.com/search?q=model+context+protocol) - MCP 学習記事
- [Elsevier API Examples](https://dev.elsevier.com/start_coding.html) - API使用例

## 📞 サポート・お問い合わせ

### 🐛 問題の報告
- **GitHub Issues**: [問題を報告する](https://github.com/yasufumi-nakata/elsevier-mcp-server/issues)
- **Feature Request**: [新機能をリクエスト](https://github.com/yasufumi-nakata/elsevier-mcp-server/issues/new)

### 💬 質問・議論
- **GitHub Discussions**: [議論に参加](https://github.com/yasufumi-nakata/elsevier-mcp-server/discussions)
- **Elsevier API サポート**: apisupport@elsevier.com

### 📝 フィードバック
プロジェクトの改善にご協力ください！
- 使用体験のレポート
- 機能追加の提案
- ドキュメントの改善案

---

## ⚖️ 利用規約・免責事項

### 📋 使用条件
- このプロジェクトは**教育・研究目的**で開発されています
- 利用者は**ElsevierのAPIの利用規約およびAI利用ポリシーのすべて**に準拠する必要があります
- **利用者の責任**: 機関および法的要件への準拠を確認する責任があります
- **データ取扱い**: 適切なデータ管理・保持ポリシーに従う責任があります

### 🛡️ 重要な免責事項
- **API準拠**: 利用者はElsevierの現行規約への準拠を独自に確認する必要があります
- **AI・倫理**: 取得データのAI訓練への使用にはElsevierの明示的な許可が必要です
- **法的責任**: ポリシー違反や誤用について作者は一切の責任を負いません
- **データ精度**: 情報の正確性はElsevierのデータ品質・ポリシーに依存します
- **商用利用**: 商用アプリケーションにはElsevierとの別途ライセンス契約が必要です

### 🚨 利用者の責任
- **規約確認**: 使用前に必ずElsevierの現行ポリシーを確認してください
- **制限遵守**: API使用制限・利用制約を厳守してください
- **適切な引用**: 取得データを使用する際は適切に出典を明記してください
- **機関コンプライアンス**: 所属機関のデータポリシーへの準拠を確認してください

### 📜 ライセンス
このプロジェクトは**MIT License**の下で公開されています。詳細は[LICENSE](LICENSE)ファイルをご確認ください。

### 🤝 貢献歓迎
プルリクエストやイシューの投稿を歓迎します！詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

---
**🔬 Elsevier MCP Server** - Academic Research Made Easier with AI
**📝 Last Updated**: 2024年12月
**🌟 GitHub**: https://github.com/yasufumi-nakata/elsevier-mcp-server