from fastapi import APIRouter

from bookings.schemas import SBooking
from bookings.services import BookingServices

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingServices.find_all()
