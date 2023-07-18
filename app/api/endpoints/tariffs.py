# endpoint for obtaining data on all tariffs
from fastapi import APIRouter

from app.api.models.tariff import Tariff

router = APIRouter()


@router.get("/tariffs/")
async def get_tariffs():
    tariffs = await Tariff.all().values()
    return tariffs
