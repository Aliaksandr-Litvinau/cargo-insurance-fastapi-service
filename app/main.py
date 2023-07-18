import datetime

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tortoise import Tortoise, fields
from tortoise.models import Model

app = FastAPI()


# # Модель для запроса
# class InsuranceRequest(BaseModel):
#     cargo_type: str
#     declared_value: float


# Модель для тарифов из БД
class Tariff(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=50)
    rate = fields.FloatField()

    class Meta:
        table = "tariffs"


# Инициализация и подключение к БД
async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Path to the SQLite database
        modules={"models": ["main"]}  # Specify the correct module path
    )
    await Tortoise.generate_schemas()


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await Tortoise.close_connections()


# Загрузка тарифов из JSON файла
def load_tariffs_from_json(file_path):
    import json
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Заполнение БД тарифами
async def fill_tariffs_in_db():
    tariffs_data = load_tariffs_from_json("tariffs.json")
    for date_str, tariffs in tariffs_data.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        for tariff_info in tariffs:
            await Tariff.create(date=date, cargo_type=tariff_info["cargo_type"], rate=tariff_info["rate"])


@app.get("/load_tariffs/")
async def load_tariffs():
    await fill_tariffs_in_db()
    return {"message": "Tariffs loaded successfully."}


# # Роут для расчета стоимости страхования
# @app.post("/calculate_insurance/")
# async def calculate_insurance(request: InsuranceRequest):
#     # Загружаем актуальный тариф из БД
#     try:
#         tariff = await Tariff.filter(cargo_type=request.cargo_type).order_by('-date').first()
#     except Tariff.DoesNotExist:
#         raise HTTPException(status_code=404, detail="Tariff not found")
#
#     # Расчет стоимости страхования
#     insurance_cost = request.declared_value * tariff.rate
#     return {"insurance_cost": insurance_cost}
