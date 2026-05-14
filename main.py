import yaml
import os
from dotenv import load_dotenv
from lib.logger import setup_logger
from agents.news_agent import NewsAgent

# 設定の読み込み
load_dotenv()
logger = setup_logger("main")

def load_config():
    with open("config/settings.yaml", "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def main():
    logger.info("日常タスクオートメーションを開始します。")
    config = load_config()

    # News Agent の実行
    if config.get("news", {}).get("hacker_news", {}).get("enabled"):
        news_config = config["news"]["hacker_news"]
        agent = NewsAgent(news_config)
        agent.run()

    # 他のエージェントも同様にここに追加可能
    # if config.get("email", {}).get("enabled"):
    #     email_agent = EmailAgent(config["email"])
    #     email_agent.run()

    logger.info("全てのタスクが完了しました。")

if __name__ == "__main__":
    main()
