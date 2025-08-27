import pytest
import time

def test_google_search(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys("Python Selenium pytest")
    search_box.send_keys("\n")
    time.sleep(3)
    assert "Python" in driver.title


import pytest
import time

@pytest.mark.parametrize("query,expected", [
    ("Python Selenium pytest", "Python"),
    ("OpenAI ChatGPT", "ChatGPT"),
    ("Selenium WebDriver", "Selenium"),
])
def test_google_search(driver, query, expected):
    driver.get("https://www.google.com")
    search_box = driver.find_element("name", "q")
    search_box.send_keys(query)
    search_box.send_keys("\n")
    time.sleep(3)
    assert expected in driver.title
