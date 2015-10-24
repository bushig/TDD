from django.test import TestCase
from django.core.urlresolvers import resolve
from lists.views import home_page

class HomePageTests(TestCase):
    def test_main_page_url(self):
        found=resolve('/')
        self.assertEqual(found,home_page)