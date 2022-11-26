from flask_testing import TestCase

from src import create_app, db


class BaseTest(TestCase):

    def create_app(self):
        return create_app('test')

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()