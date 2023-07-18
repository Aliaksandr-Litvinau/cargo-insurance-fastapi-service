# Endpoint to calculate the insurance cost
import datetime

from fastapi import HTTPException, APIRouter

from app.api.models.insurance_request import InsuranceRequest
from app.api.models.tariff import Tariff

router = APIRouter()


@router.post("/calculate_insurance/")
async def calculate_insurance(request: InsuranceRequest):
    # Parse the date from the request to a format compatible with the database
    date = datetime.datetime.strptime(request.date, "%Y-%m-%d")

    # Get the relevant tariff for the cargo type and date from the database
    try:
        tariff = await Tariff.filter(
            cargo_type=request.cargo_type,
            date__lte=date,  # use less than or equal to for the timestamp comparison
        ).order_by("-date").first()
    except Tariff.DoesNotExist:
        raise HTTPException(status_code=404, detail="Tariff not found")

    # Calculate the insurance cost
    insurance_cost = request.declared_value * tariff.rate
    return {"insurance_cost": insurance_cost}
