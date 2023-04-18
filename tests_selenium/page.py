from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from tests_selenium.locators import HomePageLocators



class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    


class HomePage(BasePage):

    def is_title_matches(self):
        return "Scraper - Home" in self.driver.title

    def is_main_heading_displayed_correctly(self):
        main_heading = self.get_element_text(HomePageLocators.MAIN_HEADING)
        text = 'This is a Python application powered by requests-HTML library to provide an efficient way to parsing HTML documents using CSS Selectors.'
        return text in main_heading

    def is_github_link_works(self):
        self.do_click(HomePageLocators.GITHUB_LINK)
        url = 'https://github.com/mjaroszewski1979'
        return url == self.driver.current_url

    def is_linkedin_link_works(self):
        self.do_click(HomePageLocators.LINKEDIN_LINK)
        url = 'https://www.linkedin.com/in/maciej-jaroszewski-0aa0451bb/'
        return url == self.driver.current_url

    def is_form_works(self):
        self.do_send_keys(HomePageLocators.WEBSITE, 'www.onet.pl')
        self.do_send_keys(HomePageLocators.KEYWORD, 'lewandowski')
        self.do_send_keys(HomePageLocators.PAGES, 2)
        self.do_click(HomePageLocators.SAVE)
        return "Scraper - Success" in self.driver.title 


class ErrorPage(BasePage):

    def is_404_page_works(self):
        return "Scraper - Page Not Found" in self.driver.title

    def is_logo_link_works(self):
        self.do_click(HomePageLocators.LOGO_LINK)
        return "Scraper - Home" in self.driver.title


   