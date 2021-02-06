import pytest
import os
from datetime import date, timedelta

from app.folder_creation import DateStamps, _folder_creation

@pytest.fixture(name="date_stamps")
def fixture_date_stamps():
    date_stamps = DateStamps()
    return date_stamps

def test_class_init(date_stamps):
    """Test is class initialization works"""
    assert date_stamps

def test_getting_today(date_stamps):
    """Test if todays date is returned"""
    assert date_stamps.get_today() == date.today()