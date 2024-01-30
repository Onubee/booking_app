from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from hotels.services import get_hotels_by_region

router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates = Jinja2Templates(directory="templates/")


@router.get("/hotels")
async def get_hotels_page(
        request: Request,
        hotels=Depends(get_hotels_by_region)
):
    return templates.TemplateResponse(
        name="hotels.html",
        context={
        "request": request,
        "hotels": hotels
        }
    )
