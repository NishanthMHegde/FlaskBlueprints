from app import db

class Todo(db.Model):
	__tablename__ = 'todos'
	tid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	done = db.Column(db.Boolean)
	description = db.Column(db.Text)

	def __repr__(self):
		return str("Name: %s , done: %s" % (self.name, self.done))

	def get_id(self):
		return self.tid