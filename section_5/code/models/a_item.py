import sqlite3
from db import db

class ItemModel(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def json(self):
		return {'name': self.name, 'price': self.price}

	@classmethod
	def find_by_name(cls, name):
		conn = sqlite3.connect('data.db')
		cursor = conn.cursor()

		query = "SELECT * FROM items WHERE name=?"
		result = cursor.execute(query, (name,))
		row = result.fetchone()
		conn.close()

		if row:
			return cls(*row) # argument unpacking cls(row[0], row[1])

	def insert(self):
		conn = sqlite3.connect('data.db')
		cursor = conn.cursor()

		query = "INSERT INTO items VALUES (?, ?)"
		cursor.execute(query, (self.name, self.price))

		conn.commit()
		conn.close()

	def update(self):
		conn = sqlite3.connect('data.db')
		cursor = conn.cursor()

		query = "UPDATE items SET price=? WHERE name=?"
		cursor.execute(query, (self.price, self.name))

		conn.commit()
		conn.close()
