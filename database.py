from peewee import *

db = SqliteDatabase('lista.db')

class Lista(Model):
    item = CharField()

    class Meta:
        database = db