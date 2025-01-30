from peewee import Model, CharField, BooleanField, SqliteDatabase, ForeignKeyField

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

class Role(Table):
    name = CharField()

class UserRole(Table):
    user = ForeignKeyField(User, on_delete="CASCADE", on_update="CASCADE")
    role = ForeignKeyField(Role, on_delete="CASCADE", on_update="CASCADE")

def create_tables():
    with database:
        database.create_tables([User, Role, UserRole])

create_tables()
