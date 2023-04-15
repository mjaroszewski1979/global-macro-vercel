from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from . import page




class GlobalMacroTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('tests_selenium/chromedriver.exe')
        
        self.driver.set_window_size(1920, 1080)

    def tearDown(self):
        self.driver.close()


    def test_home_page(self):
        self.driver.get(self.live_server_url)
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        assert home_page.is_home_heading_displayed_correctly()
        assert home_page.is_interactive_charts_link_works()
        assert home_page.is_gini_link_works()
        assert home_page.is_home_link_works()
        assert home_page.is_cpi_link_works()
        assert home_page.is_global_macro_link_works()

    def test_gini_page(self):
        self.driver.get(self.live_server_url + reverse('htmx:gini'))
        gini_page = page.GiniPage(self.driver)
        assert gini_page.is_title_matches()
        gini_page.is_select_menu_works()

    def test_cpi_page(self):
        self.driver.get(self.live_server_url + reverse('htmx:cpi'))
        cpi_page = page.CpiPage(self.driver)
        assert cpi_page.is_title_matches()
        cpi_page.is_select_menu_works()

    def test_stock_page(self):
        self.driver.get(self.live_server_url + reverse('htmx:stock'))
        cpi_page = page.StockPage(self.driver)
        assert cpi_page.is_title_matches()
        cpi_page.is_select_menu_works()


