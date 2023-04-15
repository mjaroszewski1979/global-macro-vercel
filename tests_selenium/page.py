from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import (
    HomePageLocators,
    RegisterPageLocators,
    LoginPageLocators, 
    CarsListPageLocators
)
import time



class BasePage(object):
    '''
    This is a base class to provide an interface and make sure that derived concrete classes are properly implemented. It will include 
    abstract methods neccessary to perform the most common test automation processes.
    :type name: ChromeDriver interface.
    :param object: standalone server that Selenium WebDriver uses to launch Google Chrome.
    '''

    def __init__(self, driver):
        """
        This method will automatically run to enforce upon object creation the initial web driver values. 
        :type name: ChromeDriver interface.
        :param driver: standalone server that Selenium WebDriver uses to launch Google Chrome.
        """
        self.driver = driver

    def do_clear(self, locator):
        """
        This method is used to clear text of any field, such as input field of a form.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        """
        This method is used to perform various mouse-based operations for web-application.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_login(self, username, password):
        """
        This method is used to perform login attempts with registered user credentials.
        :type name: string.
        :param username: authenticate a user when logging into web application.
        :type name: string.
        :param password: authenticate a user when logging into web application.
        """
        self.do_clear(LoginPageLocators.USERNAME_FIELD)
        self.do_clear(LoginPageLocators.PASSWORD_FIELD)
        self.do_send_keys(LoginPageLocators.USERNAME_FIELD, username)
        self.do_send_keys(LoginPageLocators.PASSWORD_FIELD, password)
        self.do_click(LoginPageLocators.LOGIN_BUTTON)

    def do_submit(self, locator):
        """
        This method is applicable only for <form> and it can be used with any element inside a form.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        """
        This is a method used to enter editable content in the text and password fields during test execution.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        :type name: string.
        :param text: keyboard input such as characters, numbers, and symbols to text boxes inside an application.
        """
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        """
        This method is used to find a unique web element within the webpage and it returns an object of type WebElement.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        """
        This method is used to find a list of unique web elements within the webpage and it returns 
        the list of web elements that match the locator value, unlike get_element, which returns only a single web element.
        :type name: Selenium locator.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        """
        This method is used to bring out the text that is visible in the HTML content. It ignores the spaces inside the HTML file.
        :param locator: address that identifies a web element uniquely within the webpage.
        """
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text


class HomePage(BasePage):
    '''
    This class will include functional tests in reference to the home page.
    All test cases are executed on Google Chrome.
    '''

    def is_title_matches(self):
        """
        This is test method to verify if the correct title is displayed.
        """
        return 'My Rides | Home Page' in self.driver.title

    def is_home_heading_displayed_correctly(self):
        """
        This is test method to verify if the correct heading is displayed.
        """
        home_heading = self.get_element_text(HomePageLocators.HOME_HEADING)
        text = 'RIDES BY MJ'
        return text in home_heading

    def is_register_link_works(self):
        """
        This is test method to verify if register page link works as expected.
        """
        self.do_click(HomePageLocators.REGISTER_LINK)
        return 'My Rides | Register' in self.driver.title

    def is_login_link_works(self):
        """
        This is test method to verify if login page link works as expected.
        """
        self.do_click(HomePageLocators.LOGIN_LINK)
        return 'My Rides | Login' in self.driver.title

    def is_home_link_works(self):
        """
        This is test method to verify if home page link works as expected.
        """
        self.do_click(HomePageLocators.HOME_LINK)
        return 'My Rides | Home Page' in self.driver.title

class RegisterPage(BasePage):

    def is_title_matches(self):
        """
        This is test method to verify if the correct title is displayed.
        """
        return 'My Rides | Register' in self.driver.title 

    def is_register_form_works(self):
        """
        This is test method to verify if the registration form works as expected when provided with
        valid data.
        """
        self.do_clear(RegisterPageLocators.USERNAME_FIELD)
        self.do_clear(RegisterPageLocators.PASSWORD1_FIELD)
        self.do_clear(RegisterPageLocators.PASSWORD2_FIELD)
        self.do_send_keys(RegisterPageLocators.USERNAME_FIELD, 'mjaroszewski')
        self.do_send_keys(RegisterPageLocators.PASSWORD1_FIELD, 'maciej_1245')
        self.do_send_keys(RegisterPageLocators.PASSWORD2_FIELD, 'maciej_1245')
        self.do_click(RegisterPageLocators.SUBMIT_BUTTON)
        return 'My Rides | Login' in self.driver.title 

class LoginPage(BasePage):

    def is_title_matches(self):
        """
        This is test method to verify if the correct title is displayed.
        """
        return 'My Rides | Login' in self.driver.title 

    def is_login_form_works(self):
        """
        This is test method to verify if the login form works as expected when provided with
        valid data.
        """
        self.do_login(username='testuser', password='12345')
        logout_text = self.get_element_text(LoginPageLocators.LOGOUT_LINK)
        return 'LOGOUT' in logout_text

    def is_logout_link_works(self):
        """
        This is test method to verify if logout link works as expected.
        """
        self.do_click(LoginPageLocators.LOGOUT_LINK)
        return 'My Rides | Home Page' in self.driver.title

class CarsListPage(BasePage):

    def is_title_matches(self):
        """
        This is test method to verify if the correct title is displayed.
        """
        return 'My Rides | Cars List' in self.driver.title 

    def is_cars_list_link_works(self):
        """
        This is test method to verify if logout link works as expected.
        """
        self.do_click(CarsListPageLocators.CARS_LIST_LINK)
        return 'My Rides | Cars List' in self.driver.title 

    def is_cars_list_heading_displayed_correctly(self):
        """
        This is test method to verify if the correct heading is displayed.
        """
        cars_list_heading = self.get_element_text(CarsListPageLocators.CARS_LIST_HEADING)
        text = 'MY CARS'
        return text in cars_list_heading

    def is_no_cars_para_displayed_correctly(self):
        """
        This is test method to verify if the correct html element is displayed in case of
        non existent user cars objects.
        """
        no_cars_para = self.get_element_text(CarsListPageLocators.NO_CARS_YET_PARA)
        text = 'YOU DO NOT HAVE CARS YET...'
        return text in no_cars_para

    def is_search_cars_form_works(self):
        """
        This is test method to verify if the serach cars form works as expected when provided with
        valid data.
        """
        self.do_clear(CarsListPageLocators.SEARCH_CARS_FIELD)
        self.do_send_keys(CarsListPageLocators.SEARCH_CARS_FIELD, 'porshe')
        self.do_click(CarsListPageLocators.ADD_CAR_BUTTON)
        car_list_item_text = self.get_element_text(CarsListPageLocators.CAR_LIST_ITEM)
        return 'PORSHE' in car_list_item_text

    def is_add_car_form_works(self):
        """
        This is test method to verify if the add car form works as expected when provided with
        valid data.
        """
        self.do_clear(CarsListPageLocators.ADD_CAR_FIELD)
        self.do_send_keys(CarsListPageLocators.ADD_CAR_FIELD, 'audi')
        self.do_click(CarsListPageLocators.ADD_CAR_SUBMIT)
        message_text = self.get_element_text(CarsListPageLocators.MESSAGE_TEXT)
        return 'ADDED AUDI TO LIST OF CARS' in message_text






    

