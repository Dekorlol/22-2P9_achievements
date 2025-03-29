from peewee import Model, CharField, SqliteDatabase, ForeignKeyField, BooleanField

database = SqliteDatabase('my_database.db')

class Table(Model):
    class Meta:
        database = database

class User(Table):
    username = CharField()
    full_name = CharField()
    hashed_password = CharField()
    disabled = BooleanField()

class Role(Table):
    name = CharField()

class UserRole(Table):
    user = ForeignKeyField(User, on_delete="CASCADE", on_update="CASCADE")
    role = ForeignKeyField(Role, on_delete="CASCADE", on_update="CASCADE")

def create_tables():
    with database:
        database.create_tables([User, Role, UserRole])

create_tables()
