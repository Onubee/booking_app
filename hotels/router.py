import asyncio
from typing import List
from fastapi import APIRouter, Query
from fastapi_cache.decorator import cache

from hotels.schemas import HotelsResponse
from hotels.services import get_hotels_by_region

router = APIRouter(
    prefix="/hotels",
    tags=["Отели"],
)


@router.get("/search/", response_model=List[HotelsResponse])
@cache(expire=20)
async def search_hotels_by_region(region: str = Query(..., title="Region", description="Name of the region")):
    await asyncio.sleep(3)
    return await get_hotels_by_region(region)
