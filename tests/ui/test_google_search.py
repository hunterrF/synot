import pytest
from pages.google_home import GoogleHomePage
from pages.google_results import GoogleResultsPage

term = "synot games"

@pytest.mark.ui
def test_google_search_synot_games(browser):
    """
    Scope: Perform a Google Search for the term "synot games".
    Verify:
      - Google Search returns results.
      - One of the top results contains the term "synot games".
    """
    home = GoogleHomePage(browser)
    home.open()
    home.accept_consent_if_present()
    home.search("synot games")

    results = GoogleResultsPage(browser)
    assert results.wait_for_results(timeout=30), "Search results did not appear."

    # Check that there are at least some result entries (via get_top_result_texts)
    top_texts = results.get_top_result_texts(top_n=8)
    assert len(top_texts) > 0, "No top results found on the page."

    # Verify at least one of top results contains "synot games"
    found, matched_text = results.any_result_equeals(term, top_n=8)
    assert found, f'None of the top results contain "synot games". Top texts: {top_texts}'