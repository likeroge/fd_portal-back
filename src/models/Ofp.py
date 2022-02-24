from mongoengine import Document, StringField, IntField, DateField, ObjectIdField, BooleanField


class Ofp(Document):
    dep = StringField()
    arr = StringField()
    last_dla = StringField(default='')
    etd = StringField()
    dof = StringField()
    ofp_airports = StringField(default='')
    meta = {
        'strict': False,
    }
