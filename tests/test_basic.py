import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import app, db

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.post(
            '/register',
            json=dict(username='testuser', password='testpassword', email='test@test.com', role='commission_manager')
        )
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.app.post(
            '/register',
            json=dict(username='testuser', password='testpassword', email='test@test.com', role='commission_manager')
        )
        response = self.app.post(
            '/login',
            headers={'Authorization': 'Basic ' + 'dGVzdHVzZXI6dGVzdHBhc3N3b3Jk'}
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
