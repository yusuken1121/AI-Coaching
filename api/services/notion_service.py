import httpx
from api.schemas.session_schema import KPTPage
from api.core.config import settings

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
        self.client = httpx.AsyncClient(headers=self.headers)

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
        title_property_name = "week_id"
        db_query_url = (
            f"https://api.notion.com/v1/databases/{self.kpt_database_id}/query"
        )
        print(f"NotionService: データベースのクエリを実行: {db_query_url}")
        print(f"NotionService: タイトルプロパティ名: {title_property_name}")
        print(f"NotionService: APIキー: {self.api_key}")
        try:
            response = await self.client.post(db_query_url)
            response.raise_for_status()
            data = response.json()
            pages = []
            for result in data.get("results", []):
                title_parts = (
                    result.get("properties", {})
                    .get(title_property_name, {})
                    .get("title", [])
                )
                page_title = (
                    title_parts[0].get("text", {}).get("content", "タイトル不明")
                    if title_parts
                    else "タイトル不明"
                )
                pages.append(
                    KPTPage(id=result["id"], url=result["url"], title=page_title)
                )
            return pages
        except Exception as e:
            print(f"NotionService: データベースのクエリに失敗: {str(e)}")
            raise e
