from django.test import TestCase, Client
from django.urls import reverse
class HelloTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello(self):
        response = self.client.get(reverse("hello-views"))
        expected_data = '<h1>Hello</h1>'
        expected_header = 'Alex'

        self.assertEqual(response.content.decode(), expected_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['name'], expected_header)

    def test_get_index(self):
        response_get = self.client.get(reverse("index-page"))


        expected_get = "Main Page"
        expected_post = "Не тот метод запроса"

        self.assertEqual(response_get.status_code, 200)

        self.assertEqual(response_get.content.decode(), expected_get)


    def test_get_contacts(self):
        response_get = self.client.get(reverse("contacts-page"))

        expected_get = "Contacts"

        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_get.content.decode(), expected_get)

    def test_get_about(self):
        response_get = self.client.get(reverse("about-page"))

        expected_get = "About"

        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_get.content.decode(), expected_get)