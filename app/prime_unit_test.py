import unittest
from flask import Flask
from prime import is_prime
from prime import app as flask_instance

import prime

class TestPrimeAPI(unittest.TestCase):

    def test_prime_17(self):
        with flask_instance.app_context():
            response = prime.is_prime(17)
        self.assertEqual(response.json, True)
        self.assertEqual(response.status_code, 200)
    
    def test_prime_36(self):
        with flask_instance.app_context():
            response = prime.is_prime(36)
        self.assertEqual(response.json, False)
        self.assertEqual(response.status_code, 200)

    def test_prime_13219(self):
        with flask_instance.app_context():
            response = prime.is_prime(13219)
        self.assertEqual(response.json, True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    with flask_instance.app_context():
        unittest.main()
