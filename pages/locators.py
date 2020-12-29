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
    MAX_SWIPE_TO_DOWNW_ACTION = 4
    TITLE_MAIN_PAGE = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/single_fragment_toolbar_wordmark')]")
    WAIT = (By.CLASS_NAME, "ant-spin-container ant-spin-blur")
    TITLE_OF_SEARCH_FIELD = (By.XPATH, "//android.widget.TextView[contains(@text, 'Search Wikipedia')]")

    TO_MY_LISTS = (By.XPATH, "//android.widget.TextView[contains(@text, 'My lists')]")

class SearchPageLocators:
    SOME_TEXT_FOR_SEARCH = "Kazan"
    SHORT_ARTICLE_TITLE = "Appium"
    DESCRIPTION_ON_OUR_SEARCH = "Capital of Tatarstan, Russia"
    MEANINGLESS_TEXT = "dfsew421234gf95"

    SEARCH_FIELD_ON_SEARCH_PAGE = (By.XPATH, "//android.widget.EditText[contains(@text, 'Search Wikipedia')]")
    CANCEL_SEARCH = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/search_close_btn')]")
    SEARCH_FIELD_EMPTY_IMAGE = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/search_empty_image')]")

    TITLE_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")
    DESCRIPTION_ON_RESULTS = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_description')]")

    BACK_FROM_SEARCH_PAGE = (By.XPATH, "//android.widget.ImageButton[contains(@index, '0')]")

class ArticlePageLocators:
    ALL_TEXT_OF_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs')]")
    TITLE_ON_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs')][0][0]")
    SHORT_DESCRIPTIONS_ON_ARTICLE = (By.XPATH, "//android.view.View[contains(@resource-id, 'pcs-edit-section-title-description')]")
    BOTTOM_OF_ARTICLE = (By.XPATH, "//android.view.View[contains(@text, 'View article in browser')]")

    SAVE_ARTICLE = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/article_menu_bookmark')]")
    BUTTON_ADD_TO_LIST = (By.XPATH, "//android.widget.Button[contains(@resource-id, 'org.wikipedia:id/snackbar_action')]")
    # BUTTON_ADD_TO_LIST = (By.XPATH, "//android.widget.FrameLayout[contains(@index, '0')]/android.widget.LinearLayout[contains(@index, '0')]/android.widget.FrameLayout[contains(@index, '0')]/android.widget.FrameLayout[contains(@resource-id, 'org.wikipedia:id/action_bar_root')]/android.widget.FrameLayout[contains(@resource-id, 'android:id/content')]/androidx.drawerlayout.widget.DrawerLayout[contains(@resource-id, 'org.wikipedia:id/navigation_drawer')]/android.widget.FrameLayout[contains(@resource-id, 'org.wikipedia:id/activity_page_container')]/android.widget.FrameLayout[contains(@resource-id, 'org.wikipedia:id/page_fragment')]/android.view.ViewGroup[contains(@resource-id, 'org.wikipedia:id/page_refresh_container')]/android.view.ViewGroup[contains(@resource-id, 'org.wikipedia:id/page_contents_container')]/android.view.ViewGroup[contains(@resource-id, 'org.wikipedia:id/fragment_page_coordinator')]/android.widget.FrameLayout[contains(@index, '0')]/android.widget.LinearLayout[contains(@index, '0')]/android.widget.Button[contains(@resource-id, 'org.wikipedia:id/snackbar_action')]")
    CREAT_NEW_LIST = (By.XPATH, "//android.widget.LinearLayout[contains(@resource-id, 'org.wikipedia:id/create_button')]")

    NAME_OF_NEW_LIST = "Test list"
    DESCRIPTION_OF_NEW_LIST = "Test description"
    NAME_OF_NEW_LIST_FIELD = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/textinput_placeholder')]")
    DESCRIPTION_OF_NEW_LIST_FIELD = (By.XPATH, "//android.widget.EditText[contains(@resource-id, 'org.wikipedia:id/secondary_text_input')]")
    BUTTON_OK_WHEN_CREATE_NEW_LIST = (By.XPATH, "//android.widget.Button[contains(@resource-id, 'android:id/button1')]")

    BUTTON_BACK_FROM_ARTICLE = (By.XPATH, "//android.widget.ImageButton[contains(@content-desc, 'Navigate up')]")

class MyListPageLocators:
    TITLE_OF_ARTICLE = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'org.wikipedia:id/page_list_item_title')]")
    MY_LIST = (By.XPATH, f"//android.widget.TextView[contains(@text, '{ArticlePageLocators.NAME_OF_NEW_LIST}')]")

    TO_OVERFLOW_MENU = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'org.wikipedia:id/item_overflow_menu')]")
    BUTTON_DELETE_LIST = (By.XPATH, f"//android.widget.TextView[contains(@text, 'Delete list')]")
    BUTTON_OK_WHEN_ALLERT_WHEN_DELETE = (By.XPATH, f"//android.widget.Button[contains(@text, 'OK')]")
