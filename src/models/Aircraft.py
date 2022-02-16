from mongoengine import Document, StringField,IntField, DateField, ObjectIdField


class Aircraft(Document):
    tail = StringField()
    water = IntField()
    fak = IntField(default=0)
    dof = IntField(default=0)
    oew = IntField()
    meta = {
        'strict': False,
    }
