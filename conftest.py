import pytest
from appium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--OS', action='store', default="android",
                     help="Choose OS: android or ios")
    parser.addoption('--language', action='store', default='fr',
                     help="Choose language")

#%LOCALAPPDATA%\Android\Sdk
#

@pytest.fixture(scope="function")
def driver(request):
    operating_system = request.config.getoption("OS")
    user_language = request.config.getoption("language")

    desired_capabilities = {}
    app_path = "C:\\Users\\Lenar\\PycharmProjects\\python-appium\\apks\\org.wikipedia.apk"
    desired_capabilities['AutomationName'] = "Appium"
    desired_capabilities['appPackage'] = "org.wikipedia"
    desired_capabilities['appActivity'] = ".main.MainActivity"
    desired_capabilities['app'] = app_path

    if operating_system == "android":
        print("\nstart android for test..")
        desired_capabilities['platformName'] = "Android"
        desired_capabilities['DeviceName'] = "AndroidTestDecice"
        desired_capabilities['platfromVersion'] = "9.0"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    elif operating_system == "ios":
        print("\nstart iOS browser for test..")
        desired_capabilities['platfomName'] = "Android"
        desired_capabilities['DeviceName'] = "AndroidTestDecice"
        desired_capabilities['platfromVersion'] = "9.0"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    else:
        raise pytest.UsageError("--OS should be android or ios")
    yield driver
    print("\nquit driver..")
    driver.quit()