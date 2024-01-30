from typing import List
from fastapi import APIRouter, Query
from hotels.schemas import HotelsResponse
from hotels.services import get_hotels_by_region

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/search/", response_model=List[HotelsResponse])
async def search_hotels_by_region(region: str = Query(..., title="Region", description="Name of the region")):
   return await get_hotels_by_region(region)
