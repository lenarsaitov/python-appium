import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, InitialSettingPageLocators
from time import sleep

class MainPage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def wait_loading(self):
        sleep(1)
        sec = 0
        while sec < 20:
            sleep(0.5)
            sec += 1
            if len(self.driver.find_elements(*MainPageLocators.WAIT)) == 0:
                break
        print(f"Loaded {sec} seconds")

    def setting_the_language(self):
        self.wait_loading()
        print(len(self.driver.find_elements(*InitialSettingPageLocators.TO_ADD_OR_EDIT_LANGUAGE)))
        self.driver.find_element(*InitialSettingPageLocators.TO_ADD_OR_EDIT_LANGUAGE).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*InitialSettingPageLocators.TO_EDIT_LANGUAGE)))
        self.driver.find_element(*InitialSettingPageLocators.TO_EDIT_LANGUAGE).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*InitialSettingPageLocators.TO_SEARCH_LANGUAGE)))
        self.driver.find_element(*InitialSettingPageLocators.TO_SEARCH_LANGUAGE).click()

        print(len(self.driver.find_elements(*InitialSettingPageLocators.SEARCH_LANGUAGE_FIELD)))
        field = self.driver.find_element(*InitialSettingPageLocators.SEARCH_LANGUAGE_FIELD)
        field.send_keys(InitialSettingPageLocators.LANGUAGE_WE_WANT)

        self.wait_loading()
        print(len(self.driver.find_elements(*InitialSettingPageLocators.LANGUAGE_WE_SELECT)))
        self.driver.find_element(*InitialSettingPageLocators.LANGUAGE_WE_SELECT).click()

        self.wait_loading()
        print(len(self.driver.find_elements(*InitialSettingPageLocators.TO_BACK)))
        self.driver.find_element(*InitialSettingPageLocators.TO_BACK).click()

    def skip_initial_settings(self):
        self.driver.find_element(*InitialSettingPageLocators.BUTTON_SKIP).click()

    def to_search_page(self):
        self.wait_loading()
        self.driver.find_element(*MainPageLocators.TITLE_OF_SEARCH_FIELD).click()

    def send_some_to_search_field(self):
        field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD_ON_SEARCH_FIELD)
        field.send_keys(MainPageLocators.SOME_TEXT_FOR_SEARCH)

    def should_be_wiki_search_field(self):
        assert len(self.driver.find_elements(*MainPageLocators.TITLE_OF_SEARCH_FIELD)) == 1

    def should_be_corresponding_results(self):
        assert len(self.driver.find_elements(*MainPageLocators.SHOULD_BE_RESULT)) == 1
