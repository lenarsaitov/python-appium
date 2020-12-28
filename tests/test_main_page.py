from pages.main_page import MainPage
import pytest

@pytest.mark.dev
def test_first(driver):
    page = MainPage(driver)
    page.setting_the_language()
    page.skip_initial_settings()