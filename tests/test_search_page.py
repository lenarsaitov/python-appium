from pages.search_page import SearchPage
from pages.base_page import BasePage
import pytest
import allure

def test_open_required_application(driver):
    page = BasePage(driver)
    page.skip_initial_settings()
    page.should_be_wiki_search_field()

@pytest.mark.search
class TestSearch:
    def test_search_on_search_field(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.should_be_corresponding_results()

    def test_cancel_search_this_theme(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.cancel_search_this_theme()
        page.should_be_empty_search_page()

    def test_cancel_any_search(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.cancel_any_search()
        page.should_be_main_page()

    def test_deep_search_on_search_field(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.to_some_result()
        page.should_be_necessary_corresponding_title()

    def test_search_return_nothing(self, driver):
        page = SearchPage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_meaningless_text()
        page.should_be_nothing_result()
