from mongoengine import *
from flask.ext.login import UserMixin

connect('pcduino', host='mongodb://pcduino:pcduino@ds031932.mongolab.com:31932/pcduino')

class User(UserMixin):
    USERS = {'roman': 'admin'}
    # login = StringField(required=True)
    # password = StringField(required=True, max_length=200)

    def __init__(self, id):
        if not id in self.USERS:
            raise UserNotFoundError()
        self.id = id
        self.password = self.USERS[id]

    @classmethod
    def get(self_class, id):
        try:
            return self_class(id)
        except UserNotFoundError:
            return None

class UserNotFoundError(Exception):
    pass
