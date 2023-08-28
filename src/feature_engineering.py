from src.processing import app_score_col_rmvd
import numpy as np
import pandas as pd


print(app_score_col_rmvd.isnull().sum().sort_values()/app_score_col_rmvd.shape[0])


'''Missing imputation => make all to be 0 missing data for proccesing'''

app_score_col_rmvd['CNT_FAM_MEMBERS'] = \
    app_score_col_rmvd['CNT_FAM_MEMBERS'].fillna(app_score_col_rmvd['CNT_FAM_MEMBERS'].mode()[0])

print(app_score_col_rmvd['CNT_FAM_MEMBERS'].isnull().sum())

print(app_score_col_rmvd.groupby(['OCCUPATION_TYPE']).size(). sort_values())

app_score_col_rmvd['OCCUPATION_TYPE'] = \
    app_score_col_rmvd['OCCUPATION_TYPE'].fillna(app_score_col_rmvd['OCCUPATION_TYPE'].mode()[0])

print(app_score_col_rmvd['OCCUPATION_TYPE'].isnull().sum())


'''missing imputation for NAME_TYPE_SUITE'''
# missing values for name type suite = 1292
print(app_score_col_rmvd['NAME_TYPE_SUITE'].isnull().sum())

print(app_score_col_rmvd.groupby(['NAME_TYPE_SUITE']).size())

app_score_col_rmvd['NAME_TYPE_SUITE'] = \
    app_score_col_rmvd['NAME_TYPE_SUITE'].fillna(app_score_col_rmvd['NAME_TYPE_SUITE'].mode()[0])

print(app_score_col_rmvd['NAME_TYPE_SUITE'].isnull().sum())

# AMT_ANNUITY
print(app_score_col_rmvd['AMT_ANNUITY'].describe())
app_score_col_rmvd['AMT_ANNUITY'] = \
    app_score_col_rmvd['AMT_ANNUITY'].fillna((app_score_col_rmvd['AMT_ANNUITY'].mean()))
print(app_score_col_rmvd['AMT_ANNUITY'].isnull().sum())

# for amt_req_credit_bureau_hour
print(app_score_col_rmvd['AMT_REQ_CREDIT_BUREAU_HOUR'].describe())
print(app_score_col_rmvd['AMT_REQ_CREDIT_BUREAU_HOUR'].unique())

amt_req_col = []

for col in app_score_col_rmvd.columns:
    if col.startswith("AMT_REQ_CREDIT_BUREAU"):
        amt_req_col.append(col)
print(amt_req_col)

for col in amt_req_col:
    app_score_col_rmvd[col] = app_score_col_rmvd[col].fillna((app_score_col_rmvd[col].median()))

    print(app_score_col_rmvd[col].isnull().sum())


# missing value for this data
print(app_score_col_rmvd['AMT_GOODS_PRICE'].agg(['min', 'max', 'median']))

app_score_col_rmvd['AMT_GOODS_PRICE'] = \
    app_score_col_rmvd['AMT_GOODS_PRICE'].fillna(app_score_col_rmvd['AMT_GOODS_PRICE'].mode()[0])

print(app_score_col_rmvd['AMT_GOODS_PRICE'].isnull().sum())
print(app_score_col_rmvd['AMT_GOODS_PRICE'].mean())

print(app_score_col_rmvd.head())
print(app_score_col_rmvd['AMT_CREDIT'].isnull().sum())




