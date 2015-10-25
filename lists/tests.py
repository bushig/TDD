from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTests(TestCase):
    def test_main_page_url(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_main_page_title(self):
        request=HttpRequest()
        response=home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>',response.content)
        self.assertTrue(response.content.endswith(b'</html>'))