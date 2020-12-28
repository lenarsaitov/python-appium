from selenium.webdriver.common.by import By

class InitialSettingPageLocators:
    TO_ADD_OR_EDIT_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@text, 'ADD OR EDIT LANGUAGES')]")
    TO_EDIT_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@text, 'LANGUAGE')]")
    TO_SEARCH_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@content-desc, 'Search for a language')]")
    SEARCH_LANGUAGE_FIELD = (By.CLASS_NAME, "android.widget.EditText")
    LANGUAGE_WE_WANT = "Русский"
    LANGUAGE_WE_SELECT = (By.XPATH, "//android.widget.TextView[contains(@text, 'Russian')]")

    TO_BACK = (By.XPATH, "//android.widget.ImageButton[contains(@content-desc, 'Navigate up')]")
    BUTTON_SKIP = (By.XPATH, "//android.widget.Button[contains(@text, 'SKIP')]")

class MainPageLocators:
    WAIT = (By.CLASS_NAME, "ant-spin-container ant-spin-blur")
    SOME_TEXT_FOR_SEARCH = "Kazan"
    TITLE_OF_SEARCH_FIELD = (By.XPATH, "//android.widget.TextView[contains(@text, 'Search Wikipedia')]")
    SEARCH_FIELD_ON_SEARCH_FIELD = (By.XPATH, "//android.widget.EditText[contains(@text, 'Search Wikipedia')]")

    TITLE_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")
    DESCRIPTION_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_description')]")