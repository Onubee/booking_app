from typing import List

from pydantic import BaseModel


class HotelsResponse(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int
