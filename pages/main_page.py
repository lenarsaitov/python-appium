from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, InitialSettingPageLocators, SearchPageLocators, ArticlePageLocators, MyListPageLocators
from allure_commons.types import AttachmentType
import allure
from time import sleep

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

    def send_some_to_search_field(self, short_article = False):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_FIELD)
        if short_article:
            field.send_keys(SearchPageLocators.SHORT_ARTICLE_TITLE)
        else:
            field.send_keys(SearchPageLocators.SOME_TEXT_FOR_SEARCH)

    def to_some_result(self, short_article = False):
        if short_article:
            self.find_element(*SearchPageLocators.TITLE_ON_RESULTS).click()
            self.wait_loading()
        else:
            self.title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
            self.description_of_results = self.find_elements(*SearchPageLocators.DESCRIPTION_ON_RESULTS)

            for i in self.description_of_results:
                if SearchPageLocators.DESCRIPTION_ON_OUR_SEARCH in i.text:
                    i.click()
                    self.wait_loading()
                    break

    def swipe_to_down(self, time_of_swipe = 3000):
        print("swiping..")
        action = TouchAction(self.driver)

        size = self.driver.get_window_size()

        start_y = int(size['height'] * 0.9)
        end_y = int(size['height'] * 0.1)

        start_x = int(size['width'] * 0.5)
        end_x = int(size['width'] * 0.5)

        self.driver.swipe(start_x, start_y, end_x, end_y, 1000)

    def swipe_to_max_down(self):
        i = 0
        self.have_bottom_element = True
        bottom_element = self.find_element(*ArticlePageLocators.BOTTOM_OF_ARTICLE)

        while i < MainPageLocators.MAX_SWIPE_TO_DOWNW_ACTION:
            try:
                WebDriverWait(self.driver, 3).until(EC.invisibility_of_element(ArticlePageLocators.BOTTOM_OF_ARTICLE))
                break
            except:
                print(i)
                i += 1
                self.swipe_to_down()

        if i >= MainPageLocators.MAX_SWIPE_TO_DOWNW_ACTION-1:
            self.have_bottom_element = False

    def add_article_to_new_test_list(self):
        self.find_element(*ArticlePageLocators.SAVE_ARTICLE).click()
        self.find_element(*ArticlePageLocators.BUTTON_ADD_TO_LIST).click()
        self.find_element(*ArticlePageLocators.CREAT_NEW_LIST).click()

        name_of_list_field = self.find_element(*ArticlePageLocators.NAME_OF_NEW_LIST_FIELD)
        name_of_list_field.send_keys(ArticlePageLocators.NAME_OF_NEW_LIST)

        description_of_list_field = self.find_element(*ArticlePageLocators.DESCRIPTION_OF_NEW_LIST_FIELD)
        description_of_list_field.send_keys(ArticlePageLocators.DESCRIPTION_OF_NEW_LIST)

        self.find_element(*ArticlePageLocators.BUTTON_OK_WHEN_CREATE_NEW_LIST).click()

    def back_from_article(self):
        self.find_element(*ArticlePageLocators.BUTTON_BACK_FROM_ARTICLE).click()

    def to_my_lists(self):
        self.find_element(*MainPageLocators.TO_MY_LISTS).click()

    def to_this_list(self):
        self.find_elements(*MyListPageLocators.MY_LIST).click()

    def delete_this_list(self):
        self.find_elements(*MyListPageLocators.TO_OVERFLOW_MENU).click()
        self.find_elements(*MyListPageLocators.BUTTON_DELETE_LIST).click()
        self.find_elements(*MyListPageLocators.BUTTON_OK_WHEN_ALLERT_WHEN_DELETE).click()

    def should_be_wiki_search_field(self):
        assert len(self.find_elements(*MainPageLocators.TITLE_OF_SEARCH_FIELD)) == 1

    def should_be_corresponding_results(self):
        title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        description_of_results = self.find_elements(*SearchPageLocators.DESCRIPTION_ON_RESULTS)
        print(f"All titles on page: {len(title_of_results)}")
        print(f"All descriptions on page: {len(description_of_results)}")

        for i in range(len(description_of_results)):
            if SearchPageLocators.SOME_TEXT_FOR_SEARCH in title_of_results[i].text and SearchPageLocators.DESCRIPTION_ON_OUR_SEARCH in description_of_results[i].text:
                assert True, "No suitable results"

    def should_be_empty_search_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 1

    def should_be_main_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 0
        assert len(self.find_elements(*MainPageLocators.TITLE_MAIN_PAGE)) == 1

    def should_be_necessary_corresponding_title(self):
        assert self.description_of_results[0].text == self.find_element(*ArticlePageLocators.SHORT_DESCRIPTIONS_ON_ARTICLE).text

    def should_be_bottom_box(self):
        assert self.have_bottom_element, "Dont have necessary bottom element"

    def should_be_my_new_list(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 1

    def should_be_article_on_this_new_list(self):
        assert self.find_element(*MyListPageLocators.TITLE_OF_ARTICLE).text == SearchPageLocators.SOME_TEXT_FOR_SEARCH

    def list_should_be_missing(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 0