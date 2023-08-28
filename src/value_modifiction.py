import pandas as pd
import numpy as np
from src.feature_engineering import app_score_col_rmvd
import seaborn as sns
import matplotlib.pyplot as plt

day_col = []
for col in app_score_col_rmvd.columns:
    if col.startswith("DAYS"):
        day_col.append(col)
    print(day_col)

for col in day_col:
    app_score_col_rmvd[col] = abs(app_score_col_rmvd[col])
    print(app_score_col_rmvd.head())

print(len(app_score_col_rmvd.columns))  # 62 columns

'''Outlier detection and treatment'''
print(app_score_col_rmvd['AMT_GOODS_PRICE'].agg(['min', 'max', 'median']))

# show in a graph data representation
sns.kdeplot(data=app_score_col_rmvd, x='AMT_GOODS_PRICE')
plt.show()
sns.boxenplot(data=app_score_col_rmvd, x='AMT_GOODS_PRICE')
plt.show()

# '''Binning the variables'''
# print(app_score_col_rmvd['AMT_CREDIT'].quantile([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.99]))
# bins = [0, 100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 9000000]
# ranges = ['0-100k', '100k-200k', '200k-300k', '300k-400k', '400k-500k', '500k-600k', '600k-700k', '700k-800k',
#           '800k-900k', 'Above 900k']
# app_score_col_rmvd['AMT_GOODS_PRICE_RANGE'] = pd.cut(app_score_col_rmvd['AMT_GOODS_PRICE'], bins, labels=ranges)
# print(app_score_col_rmvd.groupby(['AMT_GOODS_PRICE_RANGE']).size())



