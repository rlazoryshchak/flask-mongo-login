from models import User
from flask.ext.bcrypt import generate_password_hash
import sys
import mongoengine

try:
	if len(sys.argv) != 3:
		print "Wrong parameters has been set"
	else:
		User(login=sys.argv[1], password=generate_password_hash(sys.argv[2])).save()
except mongoengine.errors.NotUniqueError:
	print "User has already exist"