from pages.main_page import MainPage
import pytest

def test_open_required_application(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.should_be_wiki_search_field()

@pytest.mark.dev
def test_search_on_search_field(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.should_be_corresponding_results()