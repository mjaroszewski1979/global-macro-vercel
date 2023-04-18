from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page



class UrbanTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        
    def tearDown(self):
        self.driver.close()


    def test_home_page(self):
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_main_heading_displayed_correctly()
        assert home_page.is_github_link_works()

    def test_home_page_form(self):
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_form_works()


    def test_error_page(self):
        self.driver.get(self.live_server_url + '/some_page/')
        error_page = page.ErrorPage(self.driver)
        assert error_page.is_404_page_works()
        assert error_page.is_logo_link_works()


        