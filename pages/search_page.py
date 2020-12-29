from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators, SearchPageLocators, ArticlePageLocators
from pages.base_page import BasePage
from pages.base_page import allure_step
import allure

class SearchPage(BasePage):
    @allure_step("Переход в страницу для поиска статей")
    def to_search_page(self):
        self.find_element(*MainPageLocators.TITLE_OF_SEARCH_FIELD).click()

    @allure_step("Отмена поиска по этой теме")
    def cancel_search_this_theme(self):
        self.find_element(*SearchPageLocators.CANCEL_SEARCH).click()

    @allure_step("Возвращение из страницы поиска на главную страницу")
    def cancel_any_search(self):
        self.find_element(*SearchPageLocators.BACK_FROM_SEARCH_PAGE).click()

    def send_some_to_search_field(self, short_article = False):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_PAGE)
        if short_article:
            with allure.step(f"Ввод в поле поиска текста: {SearchPageLocators.SHORT_ARTICLE_TITLE}"):
                field.send_keys(SearchPageLocators.SHORT_ARTICLE_TITLE)
        else:
            with allure.step(f"Ввод в поле поиска текста: {SearchPageLocators.SOME_TEXT_FOR_SEARCH}"):
                field.send_keys(SearchPageLocators.SOME_TEXT_FOR_SEARCH)

    def to_some_result(self, short_article = False):
        with allure.step("Переход к статье"):
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

    @allure_step("Ввод бессмысленного текста")
    def send_meaningless_text(self):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_PAGE)
        field.send_keys(SearchPageLocators.MEANINGLESS_TEXT)

    @allure_step("Проверка наличия поля для поиска статей")
    def should_be_wiki_search_field(self):
        assert len(self.find_elements(*MainPageLocators.TITLE_OF_SEARCH_FIELD)) == 1

    @allure_step("Проверка наличия необходимых соответствующих результатов")
    def should_be_corresponding_results(self):
        title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        description_of_results = self.find_elements(*SearchPageLocators.DESCRIPTION_ON_RESULTS)
        print(f"All titles on page: {len(title_of_results)}")
        print(f"All descriptions on page: {len(description_of_results)}")

        for i in range(len(description_of_results)):
            if SearchPageLocators.SOME_TEXT_FOR_SEARCH in title_of_results[i].text and SearchPageLocators.DESCRIPTION_ON_OUR_SEARCH in description_of_results[i].text:
                assert True, "No suitable results"

    @allure_step("Проверка нахождения в пустой странице поиска")
    def should_be_empty_search_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 1

    @allure_step("Проверка появления на главной странице")
    def should_be_main_page(self):
        assert len(self.find_elements(*SearchPageLocators.SEARCH_FIELD_EMPTY_IMAGE)) == 0
        assert len(self.find_elements(*MainPageLocators.TITLE_MAIN_PAGE)) == 1

    @allure_step("Проверка наличия соответствующего заголовка и описания")
    def should_be_necessary_corresponding_title(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(ArticlePageLocators.SHORT_DESCRIPTIONS_ON_ARTICLE))
        assert self.description_of_results[0].text == self.find_element(*ArticlePageLocators.SHORT_DESCRIPTIONS_ON_ARTICLE).text

    @allure_step("Проверка отсутствия результатов поиска")
    def should_be_nothing_result(self):
        title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        assert len(title_of_results) == 0, "Should be empty results"
