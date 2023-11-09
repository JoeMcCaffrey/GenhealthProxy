from typing import List

from pydantic import BaseModel

from models.request.history_item import HistoryItem

class InferenceRequest(BaseModel):
    history: List[HistoryItem]
    num_predictions: int
    generation_length: int
    inference_threshold: float
    inference_temperature: float
