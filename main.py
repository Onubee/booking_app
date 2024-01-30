from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from bookings.router import router as booking_router
from users.router import router as user_router
from hotels.router import router as hotels_router
from pages.router import router as pages_router
from images.router import router as images_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(user_router)
app.include_router(booking_router)
app.include_router(hotels_router)
app.include_router(pages_router)
app.include_router(pages_router)
app.include_router(images_router)
