from peewee import *
import datetime

db = SqliteDatabase('blood_bank.db')

class User(Model):
    full_name = CharField()
    username = CharField()
    password = CharField()
    user_type = BooleanField()

    class Meta:
        database = db

class Donor(Model):
    name = CharField()
    age = IntegerField()
    contact = IntegerField()
    blood_type = CharField()

    class Meta:
        database=db

class Donate(Model):
    name = ForeignKeyField(Donor, backref='blood')
    blood_type = ForeignKeyField(Donor, backref='type')
    quantity = FloatField()
    date = DateField(default=datetime.date.today)

    class Meta:
        database = db

class Camp(Model):
    name = CharField()
    place = CharField()
    date = CharField()

    class Meta:
        database = db


if __name__=='__main__':
    db.connect()
    db.create_tables([User,Donor,Donate,Camp])
