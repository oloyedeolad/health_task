from datetime import datetime

from app import database


class User(database.Model):
    __tablename__ = 'Users'

    id = database.Column(database.Integer, autoincrement=True, primary_key=True)
    name = database.Column(database.String(100), nullable=False, unique=True)
    salary = database.Column(database.Integer, nullable=False)
    time_created = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<User: {}>'.format(self.name)