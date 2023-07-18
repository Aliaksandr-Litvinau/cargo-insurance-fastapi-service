# app/models/tariff.py
from tortoise import fields
from tortoise.models import Model


class Tariff(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()
    cargo_type = fields.CharField(max_length=50)
    rate = fields.FloatField()

    class Meta:
        table = "tariffs"
