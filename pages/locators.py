from selenium.webdriver.common.by import By

class MainPageLocators:
    # NEXT_ON_INITIAL_SETUP = (By.ID, "org.wikipedia:id/bottomOffset")
    WAIT = (By.CLASS_NAME, "ant-spin-container ant-spin-blur")

    # TO_ADD_OR_EDIT_LANGUAGE1 = (By.XPATH, "//span[contains(@class, 'android.widget.TextView') and text() = 'ADD OR EDIT LANGUAGES']")
    # TO_ADD_OR_EDIT_LANGUAGE2 = (By.XPATH, "//*[text() = 'ADD OR EDIT LANGUAGES']")
    # TO_ADD_OR_EDIT_LANGUAGE3 = (By.XPATH, "//*[text()[contains(.,'ADD OR EDIT LANGUAGES')]]")
    # TO_ADD_OR_EDIT_LANGUAGE4 = (By.XPATH, "//*[text()[contains(.,'ADD')]]")
    # TO_ADD_OR_EDIT_LANGUAGE5 = (By.XPATH, "//*[text()[contains(.,'EDIT LANGUAGES')]]")
    TO_ADD_OR_EDIT_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@text, 'ADD OR EDIT LANGUAGES')]")

    # TO_EDIT_LANGUAGE = (By.XPATH, "//span[contains(@class, 'android.widget.TextView') and text() = 'LANGUAGE']")
    TO_EDIT_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@text, 'LANGUAGE')]")

    # TO_SEARCH_LANGUAGE = (By.XPATH, "//android.widget.TextView[@content-desc='Search for a language']")
    TO_SEARCH_LANGUAGE = (By.XPATH, "//android.widget.TextView[contains(@content-desc, 'Search for a language')]")

    SEARCH_LANGUAGE_FIELD = (By.CLASS_NAME, "android.widget.EditText")
    LANGUAGE_WE_WANT = "Русский"
    LANGUAGE_WE_SELECT = (By.XPATH, "//android.widget.TextView[contains(@text, 'Russian')]")

    TO_BACK = (By.XPATH, "//android.widget.ImageButton[contains(@content-desc, 'Navigate up')]")
    BUTTON_SKIP = (By.XPATH, "//android.widget.Button[contains(@text, 'SKIP')]")