from flask import current_app
from flask_testing import TestCase
from flask import current_app, url_for
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        # no exist session active for user
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # def test_index_redirect(self):
    #     response = self.client.get(url_for('index'))

    #     # self.assertTrue(response.status_code == 200)

    #     self.assertRedirects(response, url_for('hello'))

    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        self.assertEqual(response.status_code, 200)

    # def test_hello_post(self):
    #     fake_form = {
    #         'username': 'fake_name',
    #         'surnames': 'fake_last_name',
    #         'email': 'email@example.com',
    #         'password': 'fake_password'
    #     }
    #     response = self.client.post(url_for('hello'), data=fake_form)
        
    #     self.assertRedirects(response, url_for('index'))    
