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

def test_have_bottom_element_on_articles(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field(short_article = True)
    page.to_some_result(short_article = True)
    page.swipe_to_max_down()
    page.should_be_bottom_box()

def test_add_article_to_list(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.to_some_result()
    page.add_article_to_new_test_list()
    page.back_from_article()
    page.cancel_search_this_theme()
    page.cancel_any_search()
    page.to_my_lists()
    page.should_be_my_new_list()
    page.to_this_list()
    page.should_be_article_on_this_new_list()
    page.delete_this_list()
    page.list_should_be_missing()

def test_search_return_nothing(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_meaningless_text()
    page.should_be_nothing_result()

@pytest.mark.dev
def test_see_article_after_rotaition(driver):
    page = MainPage(driver)
    page.skip_initial_settings()
    page.to_search_page()
    page.send_some_to_search_field()
    page.to_some_result()
    page.rotate_to_left()