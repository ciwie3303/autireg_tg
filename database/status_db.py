from peewee import *


db = SqliteDatabase('database/status.db')


class Settings(Model):
    ID = IntegerField(primary_key=True)
    status = IntegerField(default=0)
    API_token = CharField()

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()