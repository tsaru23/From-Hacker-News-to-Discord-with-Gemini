import sys
import os
from pathlib import Path
import datetime

# プロジェクトルートを検索パスに追加（直接実行時の ModuleNotFoundError 対策）
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

import httpx
from agents.base import BaseAgent
from tools.llm_client import LLMClient

class NewsAgent(BaseAgent):
    def __init__(self, config: dict):
        super().__init__("news_agent")
        self.config = config
        self.llm = LLMClient()

    def fetch_hacker_news(self):
        """Hacker News のトップストーリーを取得する。"""
        self.logger.info("Hacker News から情報を取得中...")
        try:
            top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
            response = httpx.get(top_stories_url)
            story_ids = response.json()[:self.config.get("top_n", 10)]
            
            stories = []
            for story_id in story_ids:
                item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                item_response = httpx.get(item_url)
                stories.append(item_response.json())
            
            return stories
        except Exception as e:
            self.logger.error(f"Hacker News 取得エラー: {e}")
            return []

    def run(self):
        """ニュースを収集して要約する。"""
        stories = self.fetch_hacker_news()
        if not stories:
            self.logger.warning("収集されたストーリーがありません。")
            return

        # 要約用のテキストを作成
        news_text = "\n".join([f"- {s.get('title')} ({s.get('url')})" for s in stories])
        
        self.logger.info("LLMでニュースを要約中...")
        summary = self.llm.summarize(news_text, context="Hacker News のトップ記事一覧")
        
        # 結果を保存
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = Path(f"data/summaries/news_summary_{timestamp}.md")
        output_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Hacker News 要約 ({datetime.datetime.now().strftime('%Y-%m-%d')})\n\n")
            f.write(summary)
            f.write("\n\n## 元記事一覧\n")
            f.write(news_text)

        self.logger.info(f"要約を保存しました: {output_file}")
        return summary

if __name__ == "__main__":
    # 単体実行用の簡易テスト
    import yaml
    
    # 設定の読み込み
    config_path = project_root / "config" / "settings.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        full_config = yaml.safe_load(f)
    
    news_config = full_config.get("news", {}).get("hacker_news", {})
    
    if news_config:
        agent = NewsAgent(news_config)
        agent.run()
    else:
        print("Error: Hacker News configuration not found.")
