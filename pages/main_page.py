import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators

class MainPage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def some(self):
        self.driver.find_element(*MainPageLocators.SOME)

