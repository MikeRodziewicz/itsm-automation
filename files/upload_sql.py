import pandas as pd
import sqlite3
from contextlib import contextmanager



def _make_stp_map_df():
    """Create dataframe with stp mapping"""
    stp_df = pd.read_csv('~/Documents/data_for_hs/STP_MAP.csv')
    return stp_df
