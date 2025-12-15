import re
import pytest

DOG_RANDOM_URL = "https://dog.ceo/api/breeds/image/random"
IMAGE_URL_RE = re.compile(r"^https?://.*\.(jpg|jpeg|png|gif|bmp|webp)$", re.IGNORECASE)

@pytest.mark.api
def test_dog_api_random_image(requests_session):
    resp = requests_session.get(DOG_RANDOM_URL, timeout=10)
    assert resp.status_code == 200, f"Expected 200 OK, got {resp.status_code}"
    data = resp.json()
    # API shape: {"message":"<image_url>","status":"success"}
    assert "message" in data, "Response JSON missing 'message' field"
    image_url = data["message"]
    assert isinstance(image_url, str) and image_url, "Image URL is empty or not a string"
    assert IMAGE_URL_RE.match(image_url), f"Returned URL doesn't look like an image: {image_url}"
    print("Your dog picture for today is: " + image_url)
