from selenium.webdriver.common.by import By

class HomePageLocators(object):
    
    HOME_HEADING = (By.XPATH, "//div[@id='wrapper']//div[@class='inner']//p")
    INTERACTIVE_CHARTS_LINK = (By.LINK_TEXT, 'INTERACTIVE CHARTS')
    SECTION_ONE_PARA = (By.XPATH, "//section[@id='one']//div[@class='inner']//p")
    GINI_LINK = (By.LINK_TEXT, 'GINI INDEX CHART')
    HOME_LINK = (By.LINK_TEXT, 'HOME')
    HOME_H1 = (By.XPATH, "//div[@id='wrapper']//div[@class='inner']//h1")
    CPI_LINK = (By.LINK_TEXT, 'CPI CHART')
    GLOBAL_MACRO_LINK = (By.LINK_TEXT, 'Global Macro')

class GiniPageLocators(object):
    SELECT_YEAR = (By.XPATH, "//select[@name='year']/option[text()='2015']")

class CpiPageLocators(object):
    SELECT_SYMBOL = (By.XPATH, "//select[@name='symbol']/option[text()='ITALY']")

class StockPageLocators(object):
    SELECT_STOCK = (By.XPATH, "//select[@name='stock']/option[text()='DOW JONES']")







