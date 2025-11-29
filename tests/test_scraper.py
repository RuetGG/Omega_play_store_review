import pytest

from src.scraper.reviews import get_app_info, get_app_reviews

APP_ID = "com.combanketh.mobilebanking"

def test_app_info():
    info = get_app_info(APP_ID)
    assert isinstance(info, dict)
    assert "title" in info

def test_app_reviews():
    reviews = get_app_reviews(APP_ID, count=5)
    assert isinstance(reviews, list)
    assert len(reviews) > 0
    assert "content" in reviews[0]
