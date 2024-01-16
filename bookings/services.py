from bookings.models import Bookings
from services.base import BaseService


class BookingServices(BaseService):
    model = Bookings
