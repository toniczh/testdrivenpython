from django.test import TestCase
from lists.views import home_page
from django.urls import resolve
from django.http import HttpRequest
from django.http import HttpResponse

""" class Smoketest(TestCase):
    def test_bad_math(self):
        self.assertEqual(1+1,3) """
class HomePageTest(TestCase):
    def test_url_home_page(self):
        # resolve using URL in urls.py, need to verify the difference between 
        found = resolve("/")
        self.assertEqual(found.func,home_page)
    def test_home_page_with_response(self):
        req = HttpRequest()
        res = home_page(req)
        html_page = res.content.decode('utf8')
        self.assertTrue(html_page.startswith("<html>"))
