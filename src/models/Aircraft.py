from mongoengine import Document, StringField, IntField, DateField, ObjectIdField, BooleanField


class Aircraft(Document):
    tail = StringField()
    water = IntField()
    is_water_on_board = BooleanField(default=False)
    fak = IntField(default=0)
    dof = IntField(default=0)
    oew = IntField()
    crew = IntField(default=2)
    meta = {
        'strict': False,
    }
