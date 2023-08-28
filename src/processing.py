import pandas
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.config import app, prev_app
from openpyxl.workbook import Workbook


'''data import and basic exploration'''

# print(app.head())

'''Feature selection'''

# print(app.columns)

# print(app.shape)
# missing data from dataframe
miss_data = app.isnull().sum().sort_values().reset_index()
# rename these two columns
miss_data.rename(columns={'index': 'col_name', 0: 'null_count'}, inplace=True)
print(miss_data.head())

# convert data (float 1234 => 0.00123), and export missing data xlsx file
miss_data['msng_pct'] = miss_data['null_count'] / app.shape[0] * 100
miss_data.to_excel(r"C:\\Users\\Phantom\\Desktop\\Python project\\DS\\EDA_Banking_data\\data\\missing_target.xlsx",
                   index=False)
print(miss_data.head())

# create separate dataframe for missing data => list
msng_col = miss_data[miss_data['msng_pct'] >= 40]['col_name'].to_list()
print(len(msng_col))
app_msng_rmvd = app.drop(labels=msng_col, axis=1)
print(app_msng_rmvd.shape)

print(app_msng_rmvd.head())

flag_col = []

for col in app_msng_rmvd.columns:
    if col.startswith("FLAG"):
        flag_col.append(col)

print(flag_col)
print(len(flag_col))

# show TARGET from dataframe
app_msng_rmvd[flag_col+['TARGET']].head()

flag_tgt_col = app_msng_rmvd[flag_col + ['TARGET']]
# print(flag_tgt_col.head)

'''Data processing for FLAGS'''
flag_corr = ['FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'FLAG_MOBIL', 'FLAG_EMP_PHONE', 'FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE',
             'FLAG_PHONE', 'FLAG_EMAIL', 'TARGET']
flag_corr_df = app_msng_rmvd[flag_corr]

corr_df = round(flag_corr_df.corr(), 2)

# show groups of N and Y of this dataframe
flag_corr_df['FLAG_OWN_CAR'] = flag_corr_df['FLAG_OWN_CAR'].replace({'N': 0, 'Y': 1})
flag_corr_df['FLAG_OWN_REALTY'] = flag_corr_df['FLAG_OWN_REALTY'].replace({'N': 0, 'Y': 1})

print(flag_corr_df.groupby(['FLAG_OWN_CAR']).size())

app_flag_rmvd = app_msng_rmvd.drop(labels=['FLAG_OWN_CAR', 'FLAG_OWN_REALTY', 'FLAG_MOBIL', 'FLAG_EMP_PHONE',
                                           'FLAG_WORK_PHONE', 'FLAG_CONT_MOBILE', 'FLAG_PHONE', 'FLAG_EMAIL', 'TARGET'],
                                   axis=1)
print(app_flag_rmvd.shape)
print(app_flag_rmvd.head())

app_score_col_rmvd = app_msng_rmvd[flag_col + ['TARGET']]
# app_score_col_rmvd = app_flag_rmvd.drop(['EXT_SOURCE_2', 'EXT_SOURCE_3', 'TARGET'], axis=1)
print(app_score_col_rmvd.shape)

'''*** Feature Engineering ***'''

