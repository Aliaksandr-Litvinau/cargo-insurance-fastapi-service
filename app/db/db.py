import datetime

from tortoise import Tortoise

from api.models.tariff import Tariff
from core.config import TARIFFS_JSON_FILE


# Initialization and connection to the database
async def init():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Path to the SQLite database
        modules={"models": ["api.models.tariff"]}  # Specify the correct module path
    )
    await Tortoise.generate_schemas()


# Loading tariffs from JSON file
def load_tariffs_from_json():
    import json
    with open(TARIFFS_JSON_FILE, "r") as file:
        data = json.load(file)
    return data


# Filling the database with tariffs
async def fill_tariffs_in_db():
    tariffs_data = load_tariffs_from_json()
    for date_str, tariffs in tariffs_data.items():
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        for tariff_info in tariffs:
            await Tariff.create(date=date, cargo_type=tariff_info["cargo_type"], rate=tariff_info["rate"])
