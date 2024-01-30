from sqlalchemy.future import select
from sqlalchemy import func
from database import async_session_maker
from hotels.models import Hotels
from fastapi import HTTPException


async def get_hotels_by_region(region: str):
    async with async_session_maker() as session:
        stmt = select(Hotels).where(func.lower(Hotels.location).like(func.lower(f"%{region}%")))
        result = await session.execute(stmt)
        matching_hotels = result.scalars().all()

        if not matching_hotels:
            raise HTTPException(status_code=404, detail="Hotels not found for the specified region")

        return matching_hotels
