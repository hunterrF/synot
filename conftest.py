import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def requests_session():
    session = requests.Session()
    yield session
    session.close()

@pytest.fixture(scope="function")
def browser():
    """
    Selenium WebDriver fixture using ChromeDriverManager.
    Use environment variable HEADLESS=1 to run headless.
    """
    options = Options()
    # Headless if requested
    if os.environ.get("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1600,1200")

    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(6)
    try:
        yield driver
    finally:
        try:
            driver.quit()
        except Exception:
            pass
