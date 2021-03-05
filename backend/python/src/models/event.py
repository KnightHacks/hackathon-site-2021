# -*- coding: utf-8 -*-
"""
    src.api.event
    ~~~~~~~~~~~~~

    Functions:

        create_event()
        update_event()

"""

from src import db
from src.models.sponsor import Sponsor
from src.models.user import User
from src.models import BaseDocument


class Event(BaseDocument):
    name = db.StringField(unique=True, required=True)
    date_time = db.DateTimeField(required=True)
    description = db.StringField()
    image = db.URLField()
    link = db.URLField(required=True)
    end_date_time = db.DateTimeField(required=True)
    attendees_count = db.IntField()
    event_status = db.StringField()
    sponsors = db.ListField(db.ReferenceField(Sponsor))
    user = db.ReferenceField(User)

    def to_mongo(self, *args, **kwargs):
        data = super().to_mongo(*args, **kwargs)

        data["sponsors"] = [s.sponsor_name for s in self.sponsors]

        return data
