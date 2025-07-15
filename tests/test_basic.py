import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.app import create_app, db

class BasicTests(unittest.TestCase):

    ############################
    #### setup and teardown ####
    ############################

    # executed prior to each test
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['DEBUG'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    # executed after each test
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.test_client().get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.test_client().post(
            '/register',
            json=dict(username='testuser', password='testpassword', email='test@test.com', role='commission_manager')
        )
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.app.test_client().post(
            '/register',
            json=dict(username='testuser', password='testpassword', email='test@test.com', role='commission_manager')
        )
        response = self.app.test_client().post(
            '/login',
            headers={'Authorization': 'Basic ' + 'dGVzdHVzZXI6dGVzdHBhc3N3b3Jk'}
        )
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
