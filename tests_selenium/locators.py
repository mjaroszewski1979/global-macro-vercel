from selenium.webdriver.common.by import By

class HomePageLocators(object):
    '''
    This class will include web element locators neccessary to perform home page test automation process.
    :type name: ChromeDriver interface.
    :param object: standalone server that Selenium WebDriver uses to launch Google Chrome.
    '''
    
    HOME_HEADING = (By.XPATH, "//header[@id='header']//h1")
    REGISTER_LINK = (By.LINK_TEXT, 'REGISTER')
    LOGIN_LINK = (By.LINK_TEXT, 'LOGIN')
    HOME_LINK = (By.LINK_TEXT, 'RIDES BY MJ')

class RegisterPageLocators(object):
    '''
    This class will include web element locators neccessary to perform register page test automation process.
    :type name: ChromeDriver interface.
    :param object: standalone server that Selenium WebDriver uses to launch Google Chrome.
    '''

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD1_FIELD = (By.NAME, 'password1')
    PASSWORD2_FIELD = (By.NAME, 'password2')
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='register']//section//ul[@class='actions']//input[@class='primary']")

class LoginPageLocators(object):
    '''
    This class will include web element locators neccessary to perform login page test automation process.
    :type name: ChromeDriver interface.
    :param object: standalone server that Selenium WebDriver uses to launch Google Chrome.
    '''

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, "//div[@class='login']//section//ul[@class='actions']//input[@class='primary']")
    LOGOUT_LINK = (By.LINK_TEXT, 'LOGOUT')

class CarsListPageLocators(object):
    '''
    This class will include web element locators neccessary to perform cars list page test automation process.
    :type name: ChromeDriver interface.
    :param object: standalone server that Selenium WebDriver uses to launch Google Chrome.
    '''

    CARS_LIST_HEADING = (By.XPATH, "//div[@class='car-list-main']//h3")
    CARS_LIST_LINK = (By.LINK_TEXT, 'MY CARS')
    NO_CARS_YET_PARA = (By.XPATH, "//*[@id='car-list']/div/div[2]/section[1]/p")
    SEARCH_CARS_FIELD = (By.XPATH, "//*[@id='car-list']/div/div[2]/section[2]/div[1]/input[2]")
    ADD_CAR_BUTTON = (By.XPATH, "//*[@id='results']/ul/li/span")
    CAR_LIST_ITEM = (By.XPATH, "//*[@id='car-list']/div/div[2]/section[1]/form/div[2]/li/a")
    ADD_CAR_FIELD = (By.XPATH, "//*[@id='car-list']/div/div[1]/form/input")
    ADD_CAR_SUBMIT = (By.XPATH, "//*[@id='car-list']/div/div[1]/form/button")
    MESSAGE_TEXT = (By.XPATH, "//div[@class='d-flex justify-content-between']//section//ul[@class='messages']//li")
  


    
