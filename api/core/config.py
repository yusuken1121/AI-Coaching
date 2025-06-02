# 設定管理 (APIキー、Notion DB IDなど)

import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

class Settings(BaseModel):
    NOTION_API_KEY: str = os.getenv("NOTION_API_KEY", "default_notion_api_key")
    NOTION_KPT_DATABASE_ID: str = os.getenv("NOTION_KPT_DATABASE_ID", "default_database_id")
  

settings = Settings()