import pandas as pd
from files.folder_creation import DateStamps


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
    df_for_daily_rep = pd.DataFrame(hs_data[['Ticket', 'Created', 'Score', 'Comment', 'Factor', 'Assignment Group']])
    df_for_daily_rep = pd.merge(df_for_daily_rep, stp_data, on='Assignment Group', how='left')
    return df_for_daily_rep

