# From-Hacker-News-to-Discord-with-Gemini

[日本語版はこちら](#日本語版)

## Overview
This repository is a Python-based automation framework that uses LLM agents to streamline daily information gathering and task management.

Its modular design makes it easy to add new information sources and automation tasks.

## Key Features
- **News Agent**: Automatically collects the latest information from Hacker News and technical blogs such as the Google AI Blog.
- **Agent Base**: Provides a shared foundation for building new automation agents.
- **LLM Integration**: Makes it simple to use an LLM for summarizing and analyzing collected information.

## Setup

### 1. Create the Environment
```bash
git clone https://github.com/tsaru23/From-Hacker-News-to-Discord-with-Gemini.git
cd From-Hacker-News-to-Discord-with-Gemini
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Rename `.env.example` to `.env` and add the required API keys.

```bash
cp .env.example .env
```

### 3. Run the App
```bash
python main.py
```

## Directory Structure
- `agents/`: Agents that run automation tasks.
- `config/`: System configuration, including `settings.yaml`.
- `lib/`: Shared utilities such as logging.
- `tools/`: External API integration tools such as the LLM client.

## License
MIT License

## 日本語版

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
git clone https://github.com/tsaru23/From-Hacker-News-to-Discord-with-Gemini.git
cd From-Hacker-News-to-Discord-with-Gemini
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
- `config/`: システム設定（`settings.yaml`）
- `lib/`: ロガーなどの共通ライブラリ
- `tools/`: LLMクライアントなどの外部API連携ツール

## ライセンス
MIT License
