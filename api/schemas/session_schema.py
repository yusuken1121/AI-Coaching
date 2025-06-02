from typing import Optional
from pydantic import BaseModel
class KPTWeekSessionCreateRequest(BaseModel):
  week_id:str

class KPTWeekSessionResponse(BaseModel):
  id: str # NotionページのID
  url: str # NotionページのURL
  status: Optional[str] = None
  created_at: Optional[str] = None

class KPTPage(BaseModel):
  id: str
  url: str
  title: str