from mongoengine import *

connect('pcduino', host='mongodb://pcduino:pcduino@ds031932.mongolab.com:31932/pcduino')

class User(Document):
    login = StringField(required=True)
    password = StringField(required=True, max_length=200)