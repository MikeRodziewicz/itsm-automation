import os
from datetime import date, timedelta

from files.folder_creation import DateStamps, folder_creation

def test_class_init():
    """Test is class initialization works"""
    date_stamps = DateStamps()
    assert date_stamps

def test_getting_today():
    """Test if todays date is returned"""
    date_stamps = DateStamps().get_today()
    assert date_stamps == date.today()