from api.schemas.session_schema import KPTPage
from core.config import settings

NOTION_VERSION = "2022-06-28"

class NotionService:
  # 最初に実行される
  def __init__(self):
    self.api_key = settings.NOTION_API_KEY
    self.kpt_database_id = settings.NOTION_KPT_DATABASE_ID
    self.headers = {
      "Authorization": f"Bearer {self.api_key}",
      "Content-Type": "application/json",
      "Notion-Version": NOTION_VERSION,
    }
  
  async def create_kpt_session_page(self, week_id: str) -> KPTPage:
    print(f"NotionService: week_idページを作成する: {week_id}")
    print(f"NotionService: kpt_database_id: {self.kpt_database_id}")

    # ダミーのレスポンス
    dummy_page_id = "dummy_page-id"
    dummy_page_url = f"https://www.notion.so/{dummy_page_id.replace('-', '')}"

    return KPTPage(
      id=dummy_page_id,
      url=dummy_page_url,
      title=f"Week {week_id} KPT Session",
    )
  
  async def get_kpt_session_pages(self) -> list[KPTPage]:
    print("NotionService: KPTセッションページを取得する")

    return [
      KPTPage(id="dummy-page-1", url="https://notion.so/dummy-page-1", title="2025年 第22週 KPT"),
      KPTPage(id="dummy-page-2", url="https://notion.so/dummy-page-2", title="2025年 第21週 KPT"),
    ]