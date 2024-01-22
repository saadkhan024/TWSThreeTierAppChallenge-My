from mongoengine import Document, StringField, BooleanField

class Task(Document):
    task = StringField(required=True)
    completed = BooleanField(default=False)

