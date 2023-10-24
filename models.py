# models.py
"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class User(db.Model):
    __tablename__ = "users"

    def __repr__(self):
        return f'<User id={self.id} first_name={self.first_name} last_name={self.last_name} image_url={self.image_url}>'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    first_name = db.Column(db.String, unique=True)

    last_name = db.Column(db.String, unique=True)

    image_url = db.Column(db.String)

    def greet(self):
        return f'Hi, I am {self.first_name} {self.last_name}'
 