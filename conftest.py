from selenium import webdriver
import os

class Main:
    def __init__(self):
        self.desired_capabilities = {}

    def setUp(self):
        print("Set up..")

        self.desired_capabilities['platfomName'] = "Android"
        self.desired_capabilities['DeviceName'] = "AndroidTestDecice"
        self.desired_capabilities['platfromVersion'] = "9.0"

        self.app_path = os.path.abspath("apks\org.wikipedia.apk")
        self.desired_capabilities['AutomationName'] = "Appium"
        self.desired_capabilities['appPackage'] = "org.wikipedia"
        self.desired_capabilities['appActivity'] = "main.MainActivity"
        self.desired_capabilities['app'] = self.app_path
        # self.desired_capabilities['app'] = "C:\Users\Lenar\PycharmProjects\python-appium\apks\org.wikipedia.apk"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_capabilities)

    def tearDown(self):
        print("Tear down..")
        self.driver.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--OS', action='store', default="android",
                     help="Choose OS: android or ios")
    parser.addoption('--language', action='store', default='fr',
                     help="Choose language")

@pytest.fixture(scope="function")
def driver(request):
    operating_system = request.config.getoption("OS")
    user_language = request.config.getoption("language")

    desired_capabilities = {}
    app_path = os.path.abspath("apks\org.wikipedia.apk")
    desired_capabilities['AutomationName'] = "Appium"
    desired_capabilities['appPackage'] = "org.wikipedia"
    desired_capabilities['appActivity'] = "main.MainActivity"
    desired_capabilities['app'] = app_path

    if operating_system == "android":
        print("\nstart android for test..")
        desired_capabilities['platfomName'] = "Android"
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