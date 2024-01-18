from fastapi import APIRouter, Depends

from bookings.schemas import SBooking
from bookings.services import BookingServices
from users.dependencies import get_current_user
from users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)):# -> list[SBooking]:
   return await BookingServices.find_all(user_id=1)
