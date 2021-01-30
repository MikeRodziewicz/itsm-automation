from datetime import date, timedelta
import os
import shutil


FILE_LOCATION = os.getenv('LOCATION')
TEMPLATE_LOCATION = os.getenv('LOCATION' + os.path.join('/templates'))


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


def _folder_creation(location):
    """Create a folder for all reports of the day"""
    try:
        daily_folder = os.mkdir(f'{location}/Daily_Report {DateStamps().get_today()}.xlsx')
        return daily_folder
    except FileExistsError:
        return 'File already created'

def _copy_excel_templates():
    """Copy files for excel data insert"""
    for template in TEMPLATE_LOCATION:
        shutil.copy2(template, _folder_creation(FILE_LOCATION))
    
 #TODO think about naming convention for templates   
def _rename_folders_daily():
    """Renames copied templated with the datestamp"""
    os.rename(
        f'{FILE_LOCATION}/daily_template.xlsx',
        f'{FILE_LOCATION}/CSAT Daily HS {DateStamps().get_yesterday()}.xlsx', )
    os.rename(
        f'{FILE_LOCATION}/report_maker.xlsx',
        f'{FILE_LOCATION}/report_maker {DateStamps().get_today()}.xlsx',)

def _rename_folders_weekly():
    """Rename for the weekly report"""
    os.rename(
        f'{FILE_LOCATION}/Weekly_template.xlsx',
        f'{FILE_LOCATION}/CSAT Weekly HS {DateStamps().get_yesterday()}.xlsx', )

def _rename_folders_monthly():
    """Rename for the weekly report"""
    os.rename(
        f'{FILE_LOCATION}/Monthly_template.xlsx',
        f'{FILE_LOCATION}/CSAT Monthly HS {DateStamps().get_yesterday()}.xlsx', )


def prepare_reports():
    _folder_creation(FILE_LOCATION)
    _copy_excel_templates()
    _rename_folders_daily()
    if DateStamps().time.isoweekday() == 1:
        _rename_folders_weekly()



    
