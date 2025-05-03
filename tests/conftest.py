from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope="class")
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    with webdriver.Chrome(options=options) as driver:
        request.cls.driver = driver
        yield
