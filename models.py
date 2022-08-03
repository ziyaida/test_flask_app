from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'second_db_flask',
    host = 'localhost',
    port = '5432',
    user = 'second_user_flask',
    password = '123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    name = CharField(max_length=255, null=False)
    surname = CharField(max_length=255, null=False)
    password = CharField(max_length=255, null=False)
    date = DateField(default=datetime.now)

    def __repr__(self):
        return self.name


db.close