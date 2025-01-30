from peewee import Model, CharField, BooleanField, SqliteDatabase

database = SqliteDatabase('my_database.db')

class Table(Model):
    class Meta:
        database = database

class User(Table):
    username = CharField(unique=True)
    full_name = CharField(null=True)
    email = CharField(null=True)
    hashed_password = CharField()
    disabled = BooleanField(default=False)

def create_tables():
    with database:
        database.create_tables([User])

create_tables()
