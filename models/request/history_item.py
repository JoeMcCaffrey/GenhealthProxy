from pydantic import BaseModel


class HistoryItem(BaseModel):
    code: str
    system: str
    display: str
