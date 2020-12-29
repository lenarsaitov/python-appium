from pages.article_page import ArticlePage
import pytest
import allure

@pytest.mark.article
class TestArticle:
    def test_have_bottom_element_on_articles(self, driver):
        page = ArticlePage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field(short_article = True)
        page.to_some_result(short_article = True)
        page.swipe_to_max_down()
        page.should_be_bottom_box()

    def test_add_article_to_list(self, driver):
        page = ArticlePage(driver)
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

    def test_see_article_after_background(self, driver):
        page = ArticlePage(driver)
        page.skip_initial_settings()
        page.to_search_page()
        page.send_some_to_search_field()
        page.to_background()
        page.should_be_corresponding_results()
