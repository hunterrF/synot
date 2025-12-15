from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

class GoogleHomePage:
    URL = "https://www.google.com"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def accept_consent_if_present(self):
        time.sleep(2)
        # Google may show a consent dialog in some regions; try multiple possible selectors.
        try:
            reject_button = self.driver.find_element(By.XPATH, "//button[.//div[text() = 'Odmietnuť všetko']]")
            reject_button.click()
        except Exception:
            pass
        return False

    def search(self, text):
        search_box = self.driver.find_element(By.XPATH, "//textarea[@name='q']")
        search_box.clear()
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)
