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
    TITLE_MAIN_PAGE = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/single_fragment_toolbar_wordmark')]")
    WAIT = (By.CLASS_NAME, "ant-spin-container ant-spin-blur")
    TITLE_OF_SEARCH_FIELD = (By.XPATH, "//android.widget.TextView[contains(@text, 'Search Wikipedia')]")

    ALL_TEXT_OF_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs')]")
    TITLE_ON_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs')][0][0]")
    SHORT_DESCRIPTIONS_ON_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs-edit-section-title-description')]")
    # BOTTOM_OF_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs-footer-container-legal')]")
    BOTTOM_OF_ARTICLE = (By.XPATH, "//android.view.View[contains(@text, 'View article in browser')]")
    READ_MORE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs-footer-container-readmore-heading')]")


class SearchPageLocators:
    SOME_TEXT_FOR_SEARCH = "Kazan"
    SHORT_ARTICLE_TITLE = "Appium"
    DESCRIPTION_ON_OUR_SEARCH = "Capital of Tatarstan, Russia"


    SEARCH_FIELD_ON_SEARCH_FIELD = (By.XPATH, "//android.widget.EditText[contains(@text, 'Search Wikipedia')]")
    CANCEL_SEARCH = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/search_close_btn')]")
    SEARCH_FIELD_EMPTY_IMAGE = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/search_empty_image')]")

    TITLE_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")
    DESCRIPTION_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_description')]")

    BACK_FROM_SEARCH_PAGE = (By.XPATH, "//android.widget.ImageButton[contains(@index, '0')]")
