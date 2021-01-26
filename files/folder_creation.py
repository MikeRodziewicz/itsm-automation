from datetime import date, timedelta
import os

FILE_LOCATION = os.getenv('LOCATION')


class DateStamps():
    """Create dates for data analysis and file creation"""
    
    def __init__(self):
        self.time = date.today()

    def get_today(self):
        return self.time
        
    def get_yesterday(self):
        return self.time - timedelta(days=1)

    def count_in_weekend(self):
        if self.time.isoweekday() == 1:
            the_date = self.time - timedelta(days=3)
            return the_date
        else:
            the_date = self.time - timedelta(days=1)
            return the_date

    def get_start_month(self):
        the_date = self.time.replace(day=1)
        return the_date

    def __str__(self):
        return f'today is {self.time}'


def folder_creation(location, date):
    """Create a folder for all reports of the day"""
    try:
        os.mkdir(f'{location}/Daily_Report {DateStamps().get_today()}.xlsx')
    except FileExistsError:
        return 'File already created'