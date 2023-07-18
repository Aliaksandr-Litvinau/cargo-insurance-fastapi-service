import uvicorn
from fastapi import FastAPI
from tortoise import Tortoise

from app.api.endpoints import load_tariffs
from db.db import init

app = FastAPI()

# Include your API endpoints here
app.include_router(load_tariffs.router)


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await Tortoise.close_connections()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
