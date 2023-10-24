# app.py
"""Blogly application."""

from flask import Flask, request, render_template, redirect, flash, session
from models import db, connect_db, User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

@app.route('/')
def user_listing_page():
    '''User listing''' 
    users=User.query.all()
    return render_template('user_listing.html', users=users)

@app.route('/new_user', methods=['POST'])
def new_user_page():
    '''Page with input fields for a new user'''
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    image_url = request.form.get('image_url')

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/<int:user_id>')
def user_detail_page(user_id):
    '''Page with the user details'''
    user=User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)

@app.route('/user_edit')
def user_edit_page():
    '''Page to edit user details'''


