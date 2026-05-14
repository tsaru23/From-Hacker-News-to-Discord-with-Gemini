from abc import ABC, abstractmethod
from lib.logger import setup_logger

class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.logger = setup_logger(name)

    @abstractmethod
    def run(self):
        """エージェントのメイン処理を実行する。"""
        pass
