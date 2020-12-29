from pages.search_page import SearchPage
from pages.base_page import try_except_screenshot
from config import DESCRIPTION
from config import URL_GITHUB
import pytest
import allure

@pytest.mark.search
@allure.description_html(DESCRIPTION)
@allure.testcase(URL_GITHUB, 'https://github.com/lenarsaitov/python-appium')
@allure.feature('Приложение Википедия на Android')
@allure.story('Поиск')
@allure.severity("critical")
class TestSearch:
    @pytest.mark.dev0
    @allure.title("Поле на главной странице для поиска статей")
    @try_except_screenshot
    def test_open_required_application(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.should_be_wiki_search_field()

    @allure.title("Поиск статей по конкретной теме")
    @try_except_screenshot
    def test_search_on_search_field(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.should_be_corresponding_results()

    @allure.title("Поиск статей по бессмысленной теме")
    @try_except_screenshot
    def test_search_return_nothing(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_meaningless_text()
        page.should_be_nothing_result()

    @allure.title("Открытие статьи из результатов поиска")
    @try_except_screenshot
    def test_deep_search_on_search_field(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.to_some_result()
        page.should_be_necessary_corresponding_title()

    @allure.title("Отмена поиска статей по данной теме")
    @try_except_screenshot
    def test_cancel_search_this_theme(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.cancel_search_this_theme()
        page.should_be_empty_search_page()

    @allure.title("Отмена поиска статей")
    @try_except_screenshot
    def test_cancel_any_search(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.cancel_any_search()
        page.should_be_main_page()
