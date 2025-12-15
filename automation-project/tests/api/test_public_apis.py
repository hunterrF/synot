import pytest
from urllib.parse import urlparse
from datetime import datetime

CHUCK_RANDOM_URL = "https://api.chucknorris.io/jokes/random"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"

def _is_valid_https_url(u: str) -> bool:
    try:
        p = urlparse(u)
        return p.scheme in ("http", "https") and bool(p.netloc)
    except Exception:
        return False

@pytest.mark.api
def test_chucknorris_random_joke_structure(requests_session):
    """
    Validate the structure and basic content of the response from:
    https://api.chucknorris.io/jokes/random

    Assertions:
      - HTTP 200
      - JSON contains expected top-level keys
      - 'categories' is a list
      - 'icon_url' and 'url' are valid URLs
      - 'id' and 'value' are non-empty strings
      - 'created_at' and 'updated_at' are parseable datetimes
      - 'url' should contain the returned 'id' (basic consistency check)
    """
    resp = requests_session.get(CHUCK_RANDOM_URL, timeout=10)
    assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}"

    data = resp.json()
    expected_keys = {"categories", "created_at", "icon_url", "id", "updated_at", "url", "value"}
    assert expected_keys.issubset(set(data.keys())), f"Missing keys: {expected_keys - set(data.keys())}"

    # categories
    assert isinstance(data["categories"], list), "'categories' should be a list"

    # icon_url and url
    assert isinstance(data["icon_url"], str) and data["icon_url"], "'icon_url' must be a non-empty string"
    assert _is_valid_https_url(data["icon_url"]), f"'icon_url' doesn't look like a valid URL: {data['icon_url']}"

    assert isinstance(data["url"], str) and data["url"], "'url' must be a non-empty string"
    assert _is_valid_https_url(data["url"]), f"'url' doesn't look like a valid URL: {data['url']}"

    # id and value
    assert isinstance(data["id"], str) and data["id"].strip(), "'id' must be a non-empty string"
    assert isinstance(data["value"], str) and data["value"].strip(), "'value' (joke) must be a non-empty string"

    # created_at and updated_at parsable
    try:
        created = datetime.strptime(data["created_at"], DATETIME_FORMAT)
        updated = datetime.strptime(data["updated_at"], DATETIME_FORMAT)
    except Exception as e:
        pytest.fail(f"created_at / updated_at not parsable with format {DATETIME_FORMAT}: {e}")

    # Basic consistency: the url usually ends with the id (or contains it)
    if data["id"] not in data["url"]:
        # Not a strict failure in case API changes format, but warn/assert with message
        pytest.fail(f"Expected 'url' ({data['url']}) to contain 'id' ({data['id']}) for basic consistency.")

    print("Your joke for today is:  " + data["value"])
