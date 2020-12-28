from pages.main_page import MainPage
import pytest

def test_open_required_application(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.should_be_wiki_search_field()

def test_search_on_search_field(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.should_be_corresponding_results()

def test_cancel_search_this_theme(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.cancel_search_this_theme()
    page.should_be_empty_search_page()

def test_cancel_any_search(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.cancel_any_search()
    page.should_be_main_page()

def test_deep_search_on_search_field(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.to_some_result()
    page.should_be_necessary_corresponding_title()

@pytest.mark.dev
def test_swipe_article(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field(short_article = True)
    page.to_some_result(short_article = True)
    page.swipe_to_max_down()
    page.should_be_bottom_box()