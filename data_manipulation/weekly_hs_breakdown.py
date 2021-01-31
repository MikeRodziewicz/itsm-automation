import pandas as pd
from files.folder_creation import DateStamps
from daily_report_hs import _combine_hs_and_stp


def _create_weekly_hs_base():
    """Create base dframe for weekly breakdown"""
    hs_weekly_base = _combine_hs_and_stp()
    return hs_weekly_base

def _filter_negative_hs(base_dframe):
    """Retrieve scores between 1 and 3"""
    hs_negative_df = base_dframe[base_dframe["Score"].isin([1,2,3])]
    return hs_negative_df

def _filter_neutral_hs(base_dframe):
    """Retrieve scores between 4 and 8"""
    hs_neutral_df = base_dframe[base_dframe["Score"].isin([4,5,6,7,8])]
    return hs_neutral_df

def _filter_positive_hs(base_dframe):
    """Retrieve scores between 9 and 10"""
    hs_positive_df = base_dframe[base_dframe["Score"].isin([9,10])]
    return hs_positive_df

def create_hs_breakdown(base_dfame):
    """Returns three filtered dframes"""
    hs_negative = _filter_negative_hs(base_dfame)
    hs_neutral = _filter_neutral_hs(base_dfame)
    hs_positive = _filter_positive_hs(base_dfame)

    return hs_negative, hs_neutral, hs_positive




