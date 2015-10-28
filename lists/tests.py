from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page
from django.http import HttpRequest
from django.template.loader import render_to_string

class HomePageTests(TestCase):
    def test_main_page_url(self):
        found=resolve('/')
        self.assertEqual(found.func,home_page)

    def test_main_page_returns_right_html(self):
        request=HttpRequest()
        response=home_page(request)
        expected_html=render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
