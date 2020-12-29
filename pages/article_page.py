from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, SearchPageLocators, ArticlePageLocators, MyListPageLocators
from pages.search_page import SearchPage
from pages.base_page import allure_step


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

    @allure_step("Свайп максимально вниз")
    def swipe_to_max_down(self):
        i = 0
        self.have_bottom_element = True
        bottom_element = self.find_element(*ArticlePageLocators.BOTTOM_OF_ARTICLE)

        while i < MainPageLocators.MAX_SWIPE_TO_DOWNW_ACTION:
            try:
                WebDriverWait(self.driver, 3).until(EC.invisibility_of_element(ArticlePageLocators.BOTTOM_OF_ARTICLE))
                break
            except:
                print(f"swipe {i+1}")
                i += 1
                self.swipe_to_down()

        if i >= MainPageLocators.MAX_SWIPE_TO_DOWNW_ACTION-1:
            self.have_bottom_element = False

    @allure_step("Добавление статьи в список")
    def add_article_to_new_test_list(self):
        self.find_element(*ArticlePageLocators.SAVE_ARTICLE).click()
        self.find_element(*ArticlePageLocators.BUTTON_ADD_TO_LIST).click()
        self.find_element(*ArticlePageLocators.CREAT_NEW_LIST).click()

        name_of_list_field = self.find_element(*ArticlePageLocators.NAME_OF_NEW_LIST_FIELD)
        name_of_list_field.send_keys(ArticlePageLocators.NAME_OF_NEW_LIST)

        description_of_list_field = self.find_element(*ArticlePageLocators.DESCRIPTION_OF_NEW_LIST_FIELD)
        description_of_list_field.send_keys(ArticlePageLocators.DESCRIPTION_OF_NEW_LIST)

        self.find_element(*ArticlePageLocators.BUTTON_OK_WHEN_CREATE_NEW_LIST).click()

    @allure_step("Выход из статьи")
    def back_from_article(self):
        self.find_element(*ArticlePageLocators.BUTTON_BACK_FROM_ARTICLE).click()

    @allure_step("Переход в мои списки статей")
    def to_my_lists(self):
        self.find_element(*MainPageLocators.TO_MY_LISTS).click()

    @allure_step("Переход в список")
    def to_this_list(self):
        self.find_elements(*MyListPageLocators.MY_LIST).click()

    @allure_step("Удаление данного списка")
    def delete_this_list(self):
        self.find_elements(*MyListPageLocators.TO_OVERFLOW_MENU).click()
        self.find_elements(*MyListPageLocators.BUTTON_DELETE_LIST).click()
        self.find_elements(*MyListPageLocators.BUTTON_OK_WHEN_ALLERT_WHEN_DELETE).click()

    @allure_step("Проверка наличия ссылки на переход в версию для пк")
    def should_be_bottom_box(self):
        assert self.have_bottom_element, "Dont have necessary bottom element"

    @allure_step("Проверка наличия списка")
    def should_be_my_new_list(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 1

    @allure_step("Проверка наличия статьи в списке")
    def should_be_article_on_this_new_list(self):
        assert self.find_element(*MyListPageLocators.TITLE_OF_ARTICLE).text == SearchPageLocators.SOME_TEXT_FOR_SEARCH

    @allure_step("Проверка исчезновения списка")
    def list_should_be_missing(self):
        assert len(self.find_elements(*MyListPageLocators.MY_LIST)) == 0