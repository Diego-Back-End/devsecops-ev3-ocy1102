import unittest

from app import app


class HelloRouteTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_hello_without_name(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Hello, None!')

    def test_hello_with_name(self):
        response = self.client.get('/hello?name=Diego')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), 'Hello, Diego!')


if __name__ == '__main__':
    unittest.main()
