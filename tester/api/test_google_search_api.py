import pytest
import requests

@pytest.mark.parametrize("query,expected", [
    ("Python Selenium pytest", "Python"),
    ("OpenAI ChatGPT", "ChatGPT"),
    ("Selenium WebDriver", "Selenium"),
])
def test_google_search_api(query, expected):
    # send request to Google search
    resp = requests.get("https://www.google.com/search", params={"q": query})
    assert resp.status_code == 200
    # check expected word in response body
    assert expected.lower() in resp.text.lower()
