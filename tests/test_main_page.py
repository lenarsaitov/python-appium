from pages.main_page import MainPage
import pytest
from time import sleep

@pytest.mark.dev
def test_first(driver):
    page = MainPage(driver)
    page.some()