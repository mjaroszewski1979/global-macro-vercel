from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import home_view, handler404, handler500
from .forms import MyForm
import scraper.urls
from requests_html import HTMLSession
from .scraper import GoogleScraper, GoogleLinkScraper, GoogleStatsScraper
from pathlib import Path
import os






class TestScraper(TestCase):

    def setUp(self):
        self.client = Client()

    def test_home_view_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home_view)

    def test_home_view_get(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Scraper - Home', status_code=200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_view_post(self):
        response = self.client.post(reverse('home'), {
            'website' : 'www.onet.pl',
            'keyword' : 'sport',
            'pages' : 2,
            'csv' : True
        })
        self.assertContains(response, 'Scraper - Success', status_code=200)
        self.assertTemplateUsed(response, 'success.html')

    def test_form_valid_data(self):
        form = MyForm(data={
            'website' : 'www.onet.pl',
            'keyword' : 'sport',
            'pages' : 2,
            'csv' : True
        })
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = MyForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_errorhandlers(self):
        self.assertTrue(scraper.urls.handler404.endswith('.handler404'))
        self.assertTrue(scraper.urls.handler500.endswith('.handler500'))

    def test_handler404(self):
        response = self.client.get('/404/')
        self.assertContains(response, 'Sorry, we can’t find the website you were looking for.', status_code=200)
        self.assertTemplateUsed(response, '404.html')

    def test_csv_view(self):
        response = self.client.get('/csv_view/')
        self.assertEquals(response.status_code, 200)

    def test_google_scraper(self):
        links = GoogleScraper(HTMLSession(), ".tF2Cxc", ".yuRUbf a")
        self.assertEquals(type(links.session), type(HTMLSession()))
        self.assertEquals(links.css_id_result, ".tF2Cxc")
        self.assertEquals(links.css_id_target, ".yuRUbf a")
        BASE_DIR = Path(__file__).resolve().parent.parent
        my_list = []
        my_file = 'my_file.csv'
        path = os.path.join(BASE_DIR, my_file)
        links.create_csv(my_file, my_list)
        self.assertTrue(os.path.isfile(path), True)

    def test_google_link_scraper(self):
        links = GoogleLinkScraper(HTMLSession(), ".tF2Cxc", ".yuRUbf a")
        results = []
        for item in links.get_links('www.onet.pl', 'sport', 2):
            results.append(item)
            self.assertTrue(item in results)

    def test_google_stats_scraper(self):
        stats = GoogleStatsScraper(HTMLSession(),".main", "#result-stats")
        results = []
        for item in stats.get_stats('www.wp.pl', 'lewandowski'):
            results.append(item)
            self.assertTrue(item in results)


    



   

 
   
 





