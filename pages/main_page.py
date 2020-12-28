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

    def setting_the_language(self):
        self.wait_loading()
        print(len(self.driver.find_elements(*MainPageLocators.TO_ADD_OR_EDIT_LANGUAGE)))
        self.driver.find_element(*MainPageLocators.TO_ADD_OR_EDIT_LANGUAGE).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*MainPageLocators.TO_EDIT_LANGUAGE)))
        self.driver.find_element(*MainPageLocators.TO_EDIT_LANGUAGE).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*MainPageLocators.TO_SEARCH_LANGUAGE)))
        self.driver.find_element(*MainPageLocators.TO_SEARCH_LANGUAGE).click()

        print(len(self.driver.find_elements(*MainPageLocators.SEARCH_LANGUAGE_FIELD)))
        field = self.driver.find_element(*MainPageLocators.SEARCH_LANGUAGE_FIELD)
        field.send_keys(MainPageLocators.LANGUAGE_WE_WANT)

        self.wait_loading()
        print(len(self.driver.find_elements(*MainPageLocators.LANGUAGE_WE_SELECT)))
        self.driver.find_element(*MainPageLocators.LANGUAGE_WE_SELECT).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*MainPageLocators.TO_BACK)))
        self.driver.find_element(*MainPageLocators.TO_BACK).click()

        self.wait_loading()
        # print(len(self.driver.find_elements(*MainPageLocators.BUTTON_SKIP)))
        self.driver.find_element(*MainPageLocators.BUTTON_SKIP).click()

    def skip_initial_settings(self):
        self.driver.find_element(*MainPageLocators.BUTTON_SKIP).click()
