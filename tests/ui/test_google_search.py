import pytest
from pages.google_home import GoogleHomePage
from pages.google_results import GoogleResultsPage

@pytest.mark.ui
def test_google_search_synot_games(browser):
    """
    Scope: Perform a Google Search for the term "synot games".
    Verify:
      - Google Search returns results.
      - One of the top results contains the term "synot games".
    """
    try:
        home = GoogleHomePage(browser)
        home.open()
        home.accept_consent_if_present()
        home.search("synot games")

        results = GoogleResultsPage(browser)
        assert results.wait_for_results(timeout=10), "Search results did not appear."

        top_texts = results.get_top_result_texts(top_n=8)
        assert top_texts, "No search results found."

        found, matched = results.any_result_contains("synot games", top_n=8)
        assert found, f"'synot games' not found in top results: {top_texts}"

    except Exception:
        # 🔴 Screenshot ONLY when something fails
        browser.save_screenshot("ui_test_failure.png")
        raise
