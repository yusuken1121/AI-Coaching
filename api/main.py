# main.py
from fastapi import FastAPI
from api.routers import sessions as session_router # sessions.pyをsession_routerとしてインポート
from api.core.config import settings

app = FastAPI(
    title="AIアシストKPTリフレクション API",
    description="KPTフレームワークを用いた週次振り返りを支援するAPIです。",
    version="0.1.0 (MVP)",
)

# routersディレクトリのsessions.pyで定義したルーターを登録
app.include_router(session_router.router)


@app.get("/")
async def root():
  return {"message": "Hello World"}