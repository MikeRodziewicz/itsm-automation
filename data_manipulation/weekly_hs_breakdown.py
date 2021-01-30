import pandas as pd
from files.folder_creation import DateStamps
from daily_report_hs import _combine_hs_and_stp

dframe1 = _combine_hs_and_stp()
dframe_group = pd.DataFrame(dframe1)



# print(dframe_group.groupby('Score'))
# print(dframe_group.describe())