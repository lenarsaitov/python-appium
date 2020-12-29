from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, InitialSettingPageLocators, SearchPageLocators, ArticlePageLocators, MyListPageLocators
from pages.base_page import BasePage
from pages.search_page import SearchPage

class ArticlePage(SearchPage):
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

    def should_be_bottom_box(self):
        assert self.have_bottom_element, "Dont have necessary bottom element"

    def should_be_my_new_list(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 1

    def should_be_article_on_this_new_list(self):
        assert self.find_element(*MyListPageLocators.TITLE_OF_ARTICLE).text == SearchPageLocators.SOME_TEXT_FOR_SEARCH

    def list_should_be_missing(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 0