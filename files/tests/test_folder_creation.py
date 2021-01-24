from unittest import TestCase
import os
from datetime import date, timedelta

from files.folder_creation import DateStamps

class DateCreationTest(TestCase):
    """Test creation of correct dates for the reports"""

    def setUp(self):
        self.today = date.today()

    def test_getting_today(self):
        """Test getting current date"""
        current_date = DateStamps().get_today()
        self.assertEqual(self.today, current_date)


class FileCreationTest(TestCase):
    """Test if correct files are created"""
    creation_date = '2020-20-01'
    file_location = os.getenv('LOCATION')
    
    def test_if_todays_file_created(self):
        """Check if file with todays date is created"""
        folder_creation(self.file_location, date)
        self.assertTrue(os.path.exists(f'{self.file_location}/Daily_Report{self.creation_date}.xlsx'))