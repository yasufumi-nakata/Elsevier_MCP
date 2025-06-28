# Contributing to Elsevier MCP Server

このプロジェクトへの貢献に興味を持っていただき、ありがとうございます！ 🎉

## 🤝 貢献方法

### バグ報告

バグを見つけた場合は、以下の情報を含めて[Issue](https://github.com/yourusername/elsevier-mcp-server/issues)を作成してください：

- **環境情報**:
  - OS (Windows/macOS/Linux)
  - Python バージョン
  - Cursor IDE バージョン
  - インストールした依存関係のバージョン

- **バグの詳細**:
  - 期待された動作
  - 実際の動作
  - 再現手順
  - エラーメッセージ（あれば）

### 機能リクエスト

新機能の提案は歓迎します！以下を含めてIssueを作成してください：

- 機能の説明
- なぜその機能が必要なのか
- 可能であれば、実装のアイデア

### プルリクエスト

1. **フォーク**: リポジトリをフォークしてください
2. **ブランチ作成**: 機能ブランチを作成してください
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **開発**: コードを書いてください
4. **テスト**: 変更をテストしてください
5. **コミット**: 変更をコミットしてください
   ```bash
   git commit -m 'Add some amazing feature'
   ```
6. **プッシュ**: ブランチにプッシュしてください
   ```bash
   git push origin feature/amazing-feature
   ```
7. **プルリクエスト**: GitHub上でプルリクエストを作成してください

## 📝 開発ガイドライン

### コードスタイル

- **PEP 8**: Pythonコーディング標準に従ってください
- **Type Hints**: 可能な限り型ヒントを使用してください
- **Docstrings**: 関数とクラスにdocstringを追加してください

例:
```python
def search_papers(query: str, count: int = 10) -> dict:
    """
    Scopus APIを使用して論文を検索します。

    Args:
        query: 検索クエリ
        count: 取得する論文数

    Returns:
        検索結果を含む辞書

    Raises:
        requests.RequestException: API呼び出しが失敗した場合
    """
    pass
```

### テスト

新機能やバグ修正には、適切なテストを含めてください：

```bash
# テストの実行
python test.py

# 特定の機能のテスト
python -m pytest tests/test_specific_feature.py
```

### コミットメッセージ

明確で説明的なコミットメッセージを使用してください：

- `feat:` 新機能
- `fix:` バグ修正
- `docs:` ドキュメント変更
- `style:` コードフォーマット（機能に影響しない変更）
- `refactor:` リファクタリング
- `test:` テスト追加・修正
- `chore:` ビルドプロセスやツールの変更

例:
```
feat: add institution paper statistics endpoint

- Add get_institution_papers function
- Implement year-based filtering
- Add comprehensive error handling
```

## 🔧 開発環境のセットアップ

### 1. リポジトリのクローン
```bash
git clone https://github.com/yourusername/elsevier-mcp-server.git
cd elsevier-mcp-server
```

### 2. 仮想環境の作成
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# または
venv\Scripts\activate     # Windows
```

### 3. 依存関係のインストール
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # 開発用依存関係（作成予定）
```

### 4. 環境変数の設定
```bash
export ELSEVIER_API_KEY="your_test_api_key"
```

## 📋 チェックリスト

プルリクエストを送信する前に、以下を確認してください：

- [ ] コードはPEP 8に準拠している
- [ ] 新機能にはテストが含まれている
- [ ] 既存のテストがすべてパスする
- [ ] ドキュメントが更新されている（必要に応じて）
- [ ] CHANGELOG.mdが更新されている（重要な変更の場合）

## 🏷️ ラベルの意味

Issues と Pull Requests で使用されるラベル：

- `bug`: バグ報告
- `enhancement`: 新機能・改善
- `documentation`: ドキュメント関連
- `good first issue`: 初心者向け
- `help wanted`: コミュニティの助けが必要
- `question`: 質問
- `wontfix`: 修正しない

## 📞 質問・サポート

開発に関する質問がある場合：

1. 既存のIssuesを検索してください
2. [Discussions](https://github.com/yourusername/elsevier-mcp-server/discussions)で質問してください
3. 緊急の場合は[your-email@example.com]まで連絡してください

## 📄 ライセンス

このプロジェクトに貢献することで、あなたの貢献がMITライセンスの下で公開されることに同意したものとみなされます。

---

再度、貢献に興味を持っていただき、ありがとうございます！ 🚀