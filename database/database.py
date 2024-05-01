from peewee import *


db = SqliteDatabase('database/database.db')


class Settings(Model):
    ID = IntegerField(primary_key=True)
    status = IntegerField(default=0)
    API_token = CharField()
    Country = IntegerField(default=0)
    Service = CharField()
    MaxPrice = IntegerField()

    class Meta:
        database = db


if __name__ == '__main__':

    db.connect()
