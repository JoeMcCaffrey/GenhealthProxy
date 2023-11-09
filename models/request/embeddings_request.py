from typing import List
from pydantic import BaseModel

from models.request.history_item import HistoryItem


class EmbeddingsRequest(BaseModel):
    history: List[HistoryItem]
