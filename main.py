# import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise

from app.api.endpoints.calculate_insurance_cost import router as calculate_insurance_cost_router
from app.api.endpoints.load_tariffs import router as load_tariffs_router
from app.api.endpoints.tariffs import router as tariffs_router
from app.db.db import init

app = FastAPI()

# Include your API endpoints here
app.include_router(load_tariffs_router)
app.include_router(tariffs_router)
app.include_router(calculate_insurance_cost_router)


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await Tortoise.close_connections()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
