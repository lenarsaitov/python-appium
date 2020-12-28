import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from time import sleep

class MainPage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def wait_loading(self):
        sleep(1)
        sec = 0
        while sec < 20:
            sleep(1)
            sec += 1
            if len(self.driver.find_elements(*MainPageLocators.WAIT)) == 0:
                break
        print(f"Loaded {sec} seconds")

    def some(self):
        self.wait_loading()
        self.driver.find_element(*MainPageLocators.NEXT_ON_INITIAL_SETUP).click()
        self.wait_loading()
