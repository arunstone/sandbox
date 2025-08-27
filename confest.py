# conftest.py
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # assumes chromedriver is in PATH
    yield driver
    driver.quit()
