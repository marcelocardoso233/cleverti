
from rest_framework.test import APITestCase


class TestBookSearch(APITestCase):

    def test_get_book(self):
        url = "/api/book_search"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
