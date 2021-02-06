import pandas as pd
from folder_creation import DateStamps


def _make_stp_map_df():
    """Create dataframe with stp mapping"""
    stp_df = pd.read_csv('~/Documents/data_for_hs/STP_MAP.csv')
    stp_df = pd.DataFrame(stp_df[['Assignment Group', 'STP']])
    
    return stp_df

def _read_hs_daily_data():
    """Read and return df for daily HS extract"""
    hs_daily = pd.read_csv('~/Documents/data_for_hs/hs_data.csv',header=4, skip_blank_lines=False )
    hs_daily['Created'] = pd.to_datetime(hs_daily['Created'].str[:11])

    return hs_daily

def _combine_hs_and_stp():
    """Join HS data with STP responsible"""
    hs_data = _read_hs_daily_data()
    stp_data = _make_stp_map_df()

    df_for_daily_rep = pd.DataFrame(hs_data[
        ['Ticket', 'Created', 'Score', 'Comment', 'Factor', 'Assignment Group']
    ])
    df_for_daily_rep = pd.merge(df_for_daily_rep, stp_data, on='Assignment Group', how='left')

    return df_for_daily_rep

def create_daily_HS_report():
    """Creates report for daily HS review"""
    daily_hs_rep = _combine_hs_and_stp()

    count_in_weekends = (daily_hs_rep['Created'] >= str(DateStamps().count_in_weekend()))
    daily_hs_rep = daily_hs_rep.loc[count_in_weekends]

    count_in_today = (daily_hs_rep['Created'] < str(DateStamps().get_today()))
    daily_hs_rep = daily_hs_rep.loc[count_in_today]

    return daily_hs_rep

def create_dsr_report():
    """Create two dfs to user with DSR report"""
    base_dsr_df = _combine_hs_and_stp()
    base_dsr_df = pd.DataFrame(base_dsr_df[['Created', 'Score', 'STP']])

    if DateStamps().get_today() == DateStamps().get_start_month():
        count_in_weekends = (base_dsr_df['Created'] >= str(DateStamps().count_in_weekend()))
        dsr_slide_one = base_dsr_df.loc[count_in_weekends]

    count_in_today = (base_dsr_df['Created'] < str(DateStamps().get_today()))
    dsr_slide_one = base_dsr_df.loc[count_in_today]
    dsr_slide_one = pd.DataFrame(dsr_slide_one[['Score', 'STP']])
    
    get_start_month = (base_dsr_df['Created'] >= str(DateStamps().get_start_month()))
    dsr_slide_two = base_dsr_df.loc[get_start_month]
    dsr_slide_two = base_dsr_df.loc[count_in_today]
    dsr_slide_two = pd.DataFrame(base_dsr_df[['Score', 'STP']])

    return dsr_slide_one, dsr_slide_two
