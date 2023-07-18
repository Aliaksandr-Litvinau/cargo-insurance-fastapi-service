# endpoint for obtaining data on all tariffs
from api.models.tariff import Tariff
from fastapi import APIRouter

router = APIRouter()


@router.get("/tariffs/")
async def get_tariffs():
    tariffs = await Tariff.all().values()
    return tariffs
