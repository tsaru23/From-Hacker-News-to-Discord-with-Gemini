import logging
import sys
from pathlib import Path

def setup_logger(name: str, log_file: str = "data/logs/app.log", level=logging.INFO):
    """ロガーの設定を行うユーティリティ。"""
    
    # ログフォルダの作成
    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 既存のハンドラをクリア
    if logger.hasHandlers():
        logger.handlers.clear()

    # フォーマットの設定
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 標準出力へのハンドラ
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # ファイルへのハンドラ
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
