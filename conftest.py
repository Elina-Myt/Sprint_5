import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from locators import Locators


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()

    yield driver
    driver.quit()

