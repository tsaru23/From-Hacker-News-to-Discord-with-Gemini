import os
import google.generativeai as genai
from dotenv import load_dotenv
from lib.logger import setup_logger

load_dotenv()
logger = setup_logger("llm_client")

class LLMClient:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            logger.error("GOOGLE_API_KEY が設定されていません。.env ファイルを確認してください。")
            raise ValueError("GOOGLE_API_KEY not found")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate_text(self, prompt: str, system_instruction: str = None) -> str:
        """テキストを生成する。"""
        try:
            if system_instruction:
                # システムインストラクションを反映したモデルを作成
                model = genai.GenerativeModel(
                    self.model.model_name,
                    system_instruction=system_instruction
                )
                response = model.generate_content(prompt)
            else:
                response = self.model.generate_content(prompt)
            
            return response.text
        except Exception as e:
            logger.error(f"LLM生成エラー: {e}")
            return f"Error: {e}"

    def summarize(self, text: str, context: str = "") -> str:
        """長いテキストを要約する。"""
        prompt = f"以下のテキストを要約してください。\nコンテキスト: {context}\n\nテキスト:\n{text}"
        system_instruction = "あなたはプロの編集者です。重要なポイントを箇条書きで分かりやすく要約してください。"
        return self.generate_text(prompt, system_instruction)
