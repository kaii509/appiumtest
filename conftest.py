import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.app = "/Users/khus1en/Documents/Internship Xac/PyAppiumTest/apps/LoginApp-unpacked/com.chikkanna.tgcloginapp.apk"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()
