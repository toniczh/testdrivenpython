from django.test import TestCase
from lists.views import home_page
from django.urls import resolve

""" class Smoketest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,3) """
class HomePageTest(TestCase):
    def test_url_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func,home_page)
