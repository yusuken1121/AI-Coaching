from fastapi import APIRouter, Depends, HTTPException
from typing import List # Listをインポート

from api.schemas.session_schema import (
    KPTWeekSessionCreateRequest,
    KPTWeekSessionResponse, # KPTWeekSessionResponse もインポート (実際にはKPTPageを使うかもしれないので後で調整)
    KPTPage
)
from api.services.notion_service import NotionService


router = APIRouter(
  prefix="/sessions",
  tags=["sessions"],  # APIドキュメントでのグルーピング用
)


# NotionServiceのインスタンスを依存性注入で取得するための関数
# FastAPIでは、このように書くことで、各リクエスト処理関数でNotionServiceの
# インスタンスを簡単に利用でき、テストもしやすくなります。
def get_notion_service():
    return NotionService()


@router.post("", response_model=KPTPage, status_code=201)
async def create_kpt_session(
    request_body: KPTWeekSessionCreateRequest,  
    notion_service: NotionService = Depends(get_notion_service)
):
    """
    新しい週次のKPTセッションページをNotionに作成します。

    - **week_id**: 週の識別子 (例: "2025年 第23週 KPT")
    """
    try:
        created_page = await notion_service.create_kpt_session_page(week_id= request_body.week_id)
        return created_page
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"KPTセッション作成に失敗: {str(e)}")


@router.get("", response_model=List[KPTPage], status_code=201)
async def list_kpt_sessions(
    notion_service: NotionService = Depends(get_notion_service)
):
    """
    既存のKPTセッションページの一覧を取得します。
    """
    try:
        pages = await notion_service.get_kpt_session_pages()
        return pages
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"KPTセッション取得に失敗")