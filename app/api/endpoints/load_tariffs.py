from fastapi import APIRouter

from db.db import fill_tariffs_in_db

router = APIRouter()


@router.get("/load_tariffs/")
async def load_tariffs():
    await fill_tariffs_in_db()
    return {"message": "Tariffs loaded successfully."}
