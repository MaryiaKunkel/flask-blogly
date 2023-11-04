# models.py
"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


# MODELS GO BELOW!
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, unique=True)
    last_name = db.Column(db.String, unique=True)
    image_url = db.Column(db.String)

    def __repr__(self):
        return f'<User id={self.id}, first_name "{self.first_name}", last_name "{self.last_name}", image_url "{self.image_url}">'

    def greet(self):
        return f'Hi, I am {self.first_name} {self.last_name}'
 
class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, unique=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'))

    users=db.relationship('User', backref='posts')


    def __repr__(self):
        return f'<Post id={self.id}, title "{self.title}", content "{self.content}", created_at {self.created_at}>'
    
def get_directory():
    all_posts=Post.query.all()

    for p in all_posts:
        print(p.users.first_name, p.users.last_name, p.title, p.content)
