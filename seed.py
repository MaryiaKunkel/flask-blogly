'''Seed file to make sample data for users db'''

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
johnnydepp=User(first_name='Johnny', last_name='Depp', image_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.hollywoodreporter.com%2Fnews%2Fgeneral-news%2Fjohnny-depp-is-face-christian-799861%2F&psig=AOvVaw1g59WakAcNIpmpytQARGgZ&ust=1698596469764000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCODBnIyTmYIDFQAAAAAdAAAAABAE')

# Add new objects to session, so they'll persist
db.session.add(johnnydepp)

# Commit - otherwise, this never gets saved!
db.session.commit()