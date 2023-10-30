from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class PetModelTestCase(TestCase):
    """Tests for model for Pets."""

    def setUp(self):
        """Clean up any existing pets."""

        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_greet(self):
        user = User(first_name="John", last_name="Doe", image_url="https://static.wikia.nocookie.net/john-doe-game/images/b/b2/Doe1_plus.png/revision/latest?cb=20220327075824")
        self.assertEquals(user.greet(), 'Hi, I am John Doe')


