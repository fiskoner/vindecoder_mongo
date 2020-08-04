# -*- coding: utf-8 -*-
from mongoengine import Document, fields


class Car(Document):
    _id = fields.ObjectId()
    mark = fields.StringField(null=True)
    wmi = fields.StringField(null=True)
    add_cod = fields.StringField(null=True)
    manufacturer = fields.StringField(null=True)
    mark_owner = fields.StringField(null=True)
    country_code = fields.StringField(null=True)
    country = fields.StringField(null=True)
    additional_info = fields.StringField(null=True)
    body_type = fields.StringField(null=True)
    model = fields.StringField(null=True)
    engine_capacity = fields.StringField(null=True)
    engine_kw = fields.StringField(null=True)
    color = fields.StringField(null=True)
    meta = {'collection': 'wmi'}

    class Meta:
       managed = False
       # inheritance = True

# class Car(Document):
#     meta = {'collection': 'wmi'}