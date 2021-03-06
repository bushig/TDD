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

    def test_main_page_post_requests_working(self):
        request=HttpRequest()
        request.method='POST'
        request.POST['item_text']='A new list item'

        response=home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html=render_to_string('home.html', {'new_item_text':'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)