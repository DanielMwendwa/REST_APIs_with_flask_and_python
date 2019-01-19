# A model is an internal representation of an entity
import sqlite3
from db import db

class UserModel(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, _id, username, password):
		self.id = _id
		self.username = username
		self.password = password

	@classmethod
	def find_by_username(cls, username):
		conn = sqlite3.connect('data.db')
		cursor = conn.cursor()

		query = "SELECT * FROM users WHERE username=?"
		result = cursor.execute(query, (username,))
		row = result.fetchone()
		if row:
			user = cls(*row)  #cls(row[0], row[1], row[2])
		else:
			user = None

		conn.close()
		return user


	@classmethod
	def find_by_id(cls, _id):
		conn = sqlite3.connect('data.db')
		cursor = conn.cursor()

		query = "SELECT * FROM users WHERE id=?"
		result = cursor.execute(query, (_id,))
		row = result.fetchone()
		if row:
			user = cls(*row)  #cls(row[0], row[1], row[2])
		else:
			user = None

		conn.close()
		return user