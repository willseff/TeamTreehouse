import datetime
from peewee import *
from flask.ext.login import UserMixin 
from flask.ext.bcrypt import generate_password_hash

DATABASE = SqliteDatabase('social.db')

class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=100)
	joined_at = DateTimeField(default=datetime.datetime.now)
	is_admin = BooleanField(default=False)

	class Meta:
		database = DATABASE
		# this is for if you want a view, the data will be sorted by the joined at column.
		# the '-' tells you to sort it descendingly
		order_by = ('-joined_at')

	@classmethod
	def create_user(cls, username, email, password, admin=False):
		try:
			cls.create(
				username=username,
				email=email,
				password=generate_password_hash(password),
				is_admin=admin)
		except IntegrityError:
			raise ValueError("User alread exists")

