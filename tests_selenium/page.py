from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import GiniPageLocators, HomePageLocators, CpiPageLocators, StockPageLocators
import time



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text



    


class HomePage(BasePage):

    def is_title_matches(self):
        return 'Global Macro | Home' in self.driver.title

    def is_home_heading_displayed_correctly(self):
        home_heading = self.get_element_text(HomePageLocators.HOME_HEADING)
        text = 'Investment strategy based on the interpretation and prediction of large-scale events related to national economies, history, and international relations. The strategy typically employs forecasts and analysis of interest rate trends, international trade and payments, political changes, government policies, inter-government relations, and other broad systemic factors.'
        return text in home_heading

    def is_interactive_charts_link_works(self):
        self.do_click(HomePageLocators.INTERACTIVE_CHARTS_LINK)
        section_one_para = self.get_element_text(HomePageLocators.SECTION_ONE_PARA)
        text = 'This is a measure of the distribution of income across a population. A higher Gini index indicates greater inequality, with high-income individuals receiving much larger percentages of the total income of the population.'
        return text in section_one_para

    def is_gini_link_works(self):
        self.do_click(HomePageLocators.GINI_LINK)
        return 'Global Macro | Gini Index' in self.driver.title

    def is_home_link_works(self):
        self.do_click(HomePageLocators.HOME_LINK)
        home_h1 = self.get_element_text(HomePageLocators.HOME_H1)
        text = 'Global Macro'
        return text in home_h1

    def is_cpi_link_works(self):
        self.do_click(HomePageLocators.INTERACTIVE_CHARTS_LINK)
        self.do_click(HomePageLocators.CPI_LINK)
        return 'Global Macro | CPI Index' in self.driver.title

    def is_global_macro_link_works(self):
        self.do_click(HomePageLocators.GLOBAL_MACRO_LINK)
        home_h1 = self.get_element_text(HomePageLocators.HOME_H1)
        text = 'Global Macro'
        return text in home_h1

class GiniPage(BasePage):

    def is_title_matches(self):
        return 'Global Macro | Gini Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(GiniPageLocators.SELECT_YEAR)
        time.sleep(10)

class CpiPage(BasePage):

    def is_title_matches(self):
        return 'Global Macro | CPI Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(CpiPageLocators.SELECT_SYMBOL)
        time.sleep(10)

class StockPage(BasePage):

    def is_title_matches(self):
        return 'Global Macro | Stock Index' in self.driver.title

    def is_select_menu_works(self):
        self.do_click(StockPageLocators.SELECT_STOCK)
        time.sleep(10)