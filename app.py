# app.py
"""Blogly application."""

from flask import Flask, request, render_template, redirect
from models import User, db, connect_db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///blogly"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "chickenzarecool21837"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

connect_db(app)

@app.route('/')
def redirect_to_users():
    return redirect('/users')

@app.route('/users')
def user_listing_page():
    '''User listing''' 
    users=User.query.all()
    return render_template('user_listing.html', users=users)

@app.route('/users/new')
def new_user_page():
    '''Page with input fields for a new user'''
    return render_template('new_user.html')


@app.route('/users/new', methods=['POST'])
def save_user_page():
    '''Saving the info from the inputs to the db'''
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    image_url = request.form.get('image_url')

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail_page(user_id):
    '''Page with the user details'''
    user=User.query.get_or_404(user_id)
    return render_template('user_details.html', user=user)


@app.route('/users/<int:user_id>/edit')
def user_edit_page(user_id):
    '''Page to edit user details'''
    user=User.query.get_or_404(user_id)
    return render_template('user_edit.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def save_edited_info(user_id):
    '''Save edited user details'''
    user=User.query.get_or_404(user_id)
    user.first_name = request.form.get('first_name')
    user.last_name = request.form.get('last_name')
    user.image_url = request.form.get('image_url')

    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    '''Delete user'''
    user=User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect('/users')
