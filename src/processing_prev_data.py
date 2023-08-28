import numpy as np
import pandas as pd
from src.config import prev_app
import seaborn as sns
import matplotlib.pyplot as plt
from src.processing import app_score_col_rmvd

null_count = pd.DataFrame(prev_app.isnull().sum().sort_values(ascending=False) / prev_app.shape[0] * 100). \
    reset_index().rename(columns={'index': 'var', 0: 'count_pct'})
# print(null_count)

var_msng_ge_40 = list(null_count[null_count['count_pct'] >= 40]['var'])
# print(var_msng_ge_40)
# ['RATE_INTEREST_PRIVILEGED', 'RATE_INTEREST_PRIMARY', 'AMT_DOWN_PAYMENT', 'RATE_DOWN_PAYMENT', 'NAME_TYPE_SUITE',
# 'NFLAG_INSURED_ON_APPROVAL', 'DAYS_TERMINATION', 'DAYS_LAST_DUE', 'DAYS_LAST_DUE_1ST_VERSION', 'DAYS_FIRST_DUE',
# 'DAYS_FIRST_DRAWING']

nva_cols = var_msng_ge_40 + ['RATE_INTEREST_PRIVILEGED', 'RATE_INTEREST_PRIMARY', 'AMT_DOWN_PAYMENT',
                             'RATE_DOWN_PAYMENT', 'NAME_TYPE_SUITE', 'NFLAG_INSURED_ON_APPROVAL', 'DAYS_TERMINATION',
                             'DAYS_LAST_DUE', 'DAYS_LAST_DUE_1ST_VERSION', 'DAYS_FIRST_DUE', 'DAYS_FIRST_DRAWING']
print(nva_cols)
print(len(nva_cols))
print(len(prev_app.columns))

'''Analysing the dataframe'''
prev_app_nva_col_rmvd = prev_app.drop(labels=nva_cols, axis=1)
print(len(prev_app_nva_col_rmvd))

print(prev_app_nva_col_rmvd.columns)

print(prev_app_nva_col_rmvd.head())

# check missing values
# print(prev_app_nva_col_rmvd.isnull().sum().sort_values(ascending=False)/prev_app_nva_col_rmvd.shape[0]*100)

mean_median = prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].agg(func=['mean', 'median'])
print(mean_median)

'''Fill the missing values'''
prev_app_nva_col_rmvd['AMT_GOODS_PRICE_MEDIAN'] = prev_app_nva_col_rmvd['AMT_GOODS_PRICE']. \
    fillna(prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].median())

prev_app_nva_col_rmvd['AMT_GOODS_PRICE_MEAN'] = prev_app_nva_col_rmvd['AMT_GOODS_PRICE']. \
    fillna(prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].median())

prev_app_nva_col_rmvd['AMT_GOODS_PRICE_MODE'] = prev_app_nva_col_rmvd['AMT_GOODS_PRICE']. \
    fillna(prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].median())

# get list all of these columns and create a plots
gp_cols = ['AMT_GOODS_PRICE_MODE', 'AMT_GOODS_PRICE_MEAN', 'AMT_GOODS_PRICE_MEDIAN', 'AMT_GOODS_PRICE']

# plot in the graph
# plt.figure(figsize=(10, 5))
#
# for i, col in enumerate(gp_cols):
#     plt.subplot(2, 2, i + 1)
#     sns.kdeplot(data=prev_app_nva_col_rmvd, x=col)
#     plt.subplots_adjust(wspace=0.5, hspace=0.5)
# plt.show()

# check missing data and set to 0 miss data
prev_app_nva_col_rmvd['AMT_GOODS_PRICE'] = prev_app_nva_col_rmvd['AMT_GOODS_PRICE']. \
    fillna(prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].median())

print(prev_app_nva_col_rmvd['AMT_GOODS_PRICE'].isnull().sum())

'''Show median, max and mean data from dataframe'''

prev_app_nva_col_rmvd['AMT_ANNUITY'].agg(func=['mean', 'median', 'max'])
# mean      227847.279283
# median    112320.000000
# Name: AMT_GOODS_PRICE, dtype: float64

prev_app_nva_col_rmvd['AMT_ANNUITY'] = prev_app_nva_col_rmvd['AMT_ANNUITY']. \
    fillna(prev_app_nva_col_rmvd['AMT_ANNUITY'].median())

# show me the values in the particular Product_Combination
print(prev_app_nva_col_rmvd['PRODUCT_COMBINATION'].head())

prev_app_nva_col_rmvd['PRODUCT_COMBINATION'] = prev_app_nva_col_rmvd['PRODUCT_COMBINATION']. \
    fillna(prev_app_nva_col_rmvd['PRODUCT_COMBINATION'].mode()[0])

print(prev_app_nva_col_rmvd[prev_app_nva_col_rmvd['CNT_PAYMENT'].isnull()].groupby(['NAME_CONTRACT_STATUS']).size().
      sort_values(ascending=False))

print(prev_app_nva_col_rmvd.isnull().sum().sort_values(ascending=False))

# drop data from analysis which not will be use
col_rmwd = prev_app_nva_col_rmvd.drop(labels=['AMT_GOODS_PRICE_MODE', 'AMT_GOODS_PRICE_MEAN', 'AMT_GOODS_PRICE_MEDIAN'],
                                      axis=1)
# finding the missing values
print(prev_app_nva_col_rmvd.isnull().sum().sort_values(ascending=False))
print(len(prev_app_nva_col_rmvd.columns))


