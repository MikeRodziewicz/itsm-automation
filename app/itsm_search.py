
import os 
from collections import Counter
import pandas as pd
from pandas import ExcelWriter
from daily_report_hs import _read_hs_daily_data

FILE_LOCATION = os.getenv('LOCATION')

def _inc_req_divide(base_dframe):
    """Func to separate req and inc into two Series"""
    base_dframe = base_dframe[['Ticket', 'Ticket Type']]
    inident_dframe = base_dframe.loc[base_dframe['Ticket Type'] == 'Incident']
    request_dframe = base_dframe.loc[base_dframe['Ticket Type'] == 'Request']
    return inident_dframe, request_dframe

def write_search_strings():
    """Func to wrtie itsm searches for inc and req"""
    inc, req = _inc_req_divide(_read_hs_daily_data())
    inc_list = list(inc['Ticket'].values.flatten())
    req_list = list(req['Ticket'].values.flatten())

    with open(f'{FILE_LOCATION}/inc_search.txt') as inc_txt:
        for reference in inc_list:
            inc_txt.write(f"""'Associated Request ID' = "{cell.value}" OR """)
        inc_txt.seek(0, 2)
        inc_txt.seek(inc_txt.tell() - 3, 0)
        inc_txt.truncate()

    with open(f'{FILE_LOCATION}/req_search.txt') as req_txt:
        for reference in req_list:
             req_txt.write(f"""'Service Request ID' = "{cell.value}" OR """)
        wo_txt.seek(0,2)
        wo_txt.seek(wo_txt.tell() -3,0)
        wo_txt.truncate()


def _string_splitter():
    """Read excel file to get a list of factors"""
    try:
        df = pd.read_excel(f"{location}/HS_data.xlsx",sheet_name='Sheet1')
        df_new = df[df['Factor'].notnull()]
        list_of_factors = df_new['Factor'].tolist()
        split_list_factors = []
        for item in list_of_factors:
            split_list_factors.extend(item.split(', '))
        return split_list_factors
    except FileNotFoundError:
        print('no such file')

        
def factor_counter(raw_list):
    """Get a list of factors and calculate statistics write to a file"""
    calculated_list = Counter(raw_list).most_common() 
    with open(f"{dst}/hs_calculations.txt", 'w') as hs_cal:
        for item in calculated_list:
            hs_cal.write(f'{item} \n')
    
