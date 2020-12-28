import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, InitialSettingPageLocators, SearchPageLocators
from time import sleep

class MainPage:
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

    def to_search_page(self):
        self.find_element(*MainPageLocators.TITLE_OF_SEARCH_FIELD).click()

    def cancel_search_this_theme(self):
        self.find_element(*SearchPageLocators.CANCEL_SEARCH).click()

    def cancel_any_search(self):
        self.find_element(*SearchPageLocators.BACK_FROM_SEARCH_PAGE).click()

    def send_some_to_search_field(self):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_FIELD)
        field.send_keys(SearchPageLocators.SOME_TEXT_FOR_SEARCH)

    def to_some_result(self):
        self.title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        self.description_of_results = self.find_elements(*SearchPageLocators.DESCRIPTION_ON_RESULTS)

        for i in self.description_of_results:
            if SearchPageLocators.DESCRIPTION_ON_OUR_SEARCH in i.text:
                i.click()
                break

    def should_be_wiki_search_field(self):
        assert len(self.find_elements(*MainPageLocators.TITLE_OF_SEARCH_FIELD)) == 1

    def should_be_corresponding_results(self):
        title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        description_of_results = self.find_elements(*SearchPageLocators.DESCRIPTION_ON_RESULTS)
        print(f"All titles on page: {len(title_of_results)}")
        print(f"All descriptions on page: {len(description_of_results)}")
        trues = 0

        for i in title_of_results:
            if SearchPageLocators.SOME_TEXT_FOR_SEARCH in i.text:
                trues +=1
                break

        for i in description_of_results:
            if SearchPageLocators.DESCRIPTION_ON_OUR_SEARCH in i.text:
                trues +=1
                break

        if trues !=2 :
            assert False, "No suitable results"

    def should_be_empty_search_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 1

    def should_be_main_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 0
        assert len(self.find_elements(*MainPageLocators.TITLE_MAIN_PAGE)) == 1

    def should_be_necessary_corresponding_title(self):
        assert self.description_of_results[0].text == self.find_element(*MainPageLocators.SHORT_DESCRIPTIONS_ON_ARTICLE).text