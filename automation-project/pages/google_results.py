from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class GoogleResultsPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_results(self, timeout=30):
        # basic wait by polling for search results container
        end = time.time() + timeout
        while time.time() < end:
            try:
                # Search results commonly appear under div#search or div#rso
                if self.driver.find_elements(By.CSS_SELECTOR, "div#search, div#rso, div.g"):
                    return True
            except Exception:
                pass
            time.sleep(0.5)
        return False

    def get_top_result_texts(self, top_n=10):
        """
        Returns text snippets/titles of top N results.
        """
        results = []
        elems = self.driver.find_elements(By.XPATH, "//h3")
        for e in elems[:top_n]:
            try:
                results.append(e.text.strip())
            except Exception:
                # fallback to whole element text
                results.append(e.text.strip())
        return results

    def any_result_equeals(self, term, top_n=10):
        term = term.lower()
        texts = self.get_top_result_texts(top_n=top_n)
        i=0
        for t in texts:
            i+=1
            if term == t.lower():
                print("Searach result " + t + " is " + str(i) +" from top.")
                return True, t
        return False, None
