# Create your tests here.
from django.test import RequestFactory, TestCase

from .views import index, stringMatchPercentage

class TestKeyValueMatching(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()


    def test_index_page(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')

        # Test index() as if it were deployed at /
        response = index(request)
        self.assertEqual(response.status_code, 200)

    
    def test_index_page(self):
        # Create an instance of a POST request.
        request = self.factory.post('/string-match-percentage', data = {'key': 'SODIUM CHLORIDE 0.9% MINIMS EYE DROPS'})

        # Test stringMatchPercentage() as if it were deployed at /string-match-percentage
        response = stringMatchPercentage(request)
        self.assertEqual(response.status_code, 200)
