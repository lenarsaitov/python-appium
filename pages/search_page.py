from pages.locators import MainPageLocators, InitialSettingPageLocators, SearchPageLocators, ArticlePageLocators, MyListPageLocators
from pages.base_page import BasePage
from allure_commons.types import AttachmentType
import allure
from time import sleep

class SearchPage(BasePage):
    def to_search_page(self):
        self.find_element(*MainPageLocators.TITLE_OF_SEARCH_FIELD).click()

    def cancel_search_this_theme(self):
        self.find_element(*SearchPageLocators.CANCEL_SEARCH).click()

    def cancel_any_search(self):
        self.find_element(*SearchPageLocators.BACK_FROM_SEARCH_PAGE).click()

    def send_some_to_search_field(self, short_article = False):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_PAGE)
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

    def send_meaningless_text(self):
        field = self.find_element(*SearchPageLocators.SEARCH_FIELD_ON_SEARCH_PAGE)
        field.send_keys(SearchPageLocators.MEANINGLESS_TEXT)

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

    def should_be_nothing_result(self):
        title_of_results = self.find_elements(*SearchPageLocators.TITLE_ON_RESULTS)
        assert len(title_of_results) == 0, "Should be empty results"
