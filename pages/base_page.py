from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, InitialSettingPageLocators
from allure_commons.types import AttachmentType
import allure

def allure_step(description):
    def decorator_for_step(function):
        def wrapped(*args):
            with allure.step(description):
                function(*args)
        return wrapped
    return decorator_for_step

def try_except_screenshot(function):
    def wrapped(self, web_driver):
        try:
            function(self, web_driver)
            allure.attach(web_driver.get_screenshot_as_png(), name='Скриншот', attachment_type=AttachmentType.PNG)
        except AssertionError:
            allure.attach(web_driver.get_screenshot_as_png(), name='Ошибка в тестируемом объекте', attachment_type=AttachmentType.PNG)
            raise
        except:
            allure.attach(web_driver.get_screenshot_as_png(), name='Ошибка в тесте', attachment_type=AttachmentType.PNG)
            raise
    return wrapped

class BasePage:
    def __init__(self, driver, timeout = 10):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def wait_loading(self):
        sec = 0
        while sec < 20:
            sleep(0.1)
            if len(self.driver.find_elements(*MainPageLocators.WAIT)) == 0:
                break
            sec += 1
        if sec > 0:
            print(f"Loaded {sec} seconds")

    def find_element(self, how, what, click = False, timeout = 10):
        self.wait_loading()
        if click == True:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        else:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))

    def find_elements(self, how, what, timeout = 10):
        self.wait_loading()
        return self.driver.find_elements(how, what)
        # return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((how, what)))

    def setting_the_language(self):
        self.find_element(*InitialSettingPageLocators.TO_ADD_OR_EDIT_LANGUAGE).click()
        self.find_element(*InitialSettingPageLocators.TO_EDIT_LANGUAGE).click()
        self.find_element(*InitialSettingPageLocators.TO_SEARCH_LANGUAGE).click()

        field = self.find_element(*InitialSettingPageLocators.SEARCH_LANGUAGE_FIELD)
        field.send_keys(InitialSettingPageLocators.LANGUAGE_WE_WANT)

        self.find_element(*InitialSettingPageLocators.LANGUAGE_WE_SELECT).click()
        self.find_element(*InitialSettingPageLocators.TO_BACK).click()

    def skip_initial_settings(self):
        self.find_element(*InitialSettingPageLocators.BUTTON_SKIP).click()

    def to_background(self):
        self.driver.background_app(2)

    def should_be_wiki_search_field(self):
        assert len(self.find_elements(*MainPageLocators.TITLE_OF_SEARCH_FIELD)) == 1