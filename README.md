# Daily Task Automation (Public Version)

## 概要
このリポジトリは、LLM（大規模言語モデル）エージェントを活用して、日々の情報収集やタスク管理を効率化するためのPythonベースの自動化フレームワークです。

モジュール化された設計により、新しい収集ソースや自動化タスクを簡単に追加することができます。

## 主な機能
- **News Agent**: Hacker Newsや技術ブログ（Google AI Blog等）から最新情報を自動収集します。
- **Agent Base**: 新しい自動化エージェントを開発するための共通基盤を提供します。
- **LLM Integration**: 収集した情報の要約や分析にLLMを簡単に組み込めます。

## セットアップ

### 1. 環境構築
```bash
git clone https://github.com/YOUR_USERNAME/daily-task-automation-public.git
cd daily-task-automation-public
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 設定
`.env.example` を `.env` にリネームし、必要なAPIキーを設定してください。

```bash
cp .env.example .env
```

### 3. 実行
```bash
python main.py
```

## フォルダ構成
- `agents/`: 自動化タスクを実行するエージェント群
- `config/`: システム設定 (settings.yaml)
- `lib/`: 共通ライブラリ（ロガー等）
- `tools/`: 外部API連携ツール（LLMクライアント等）

## ライセンス
MIT License
