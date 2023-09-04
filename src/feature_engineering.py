from src.processing import app_score_col_rmvd
import numpy as np
import pandas as pd

"""This line calculates the percentage of missing values in each column of the app_score_col_rmvd DataFrame, 
sorts them in ascending order, and prints the result."""
print(app_score_col_rmvd.isnull().sum().sort_values()/app_score_col_rmvd.shape[0])


'''Missing imputation => make all to be 0 missing data for proccesing'''
"""This line fills missing values in the 'CNT_FAM_MEMBERS' column with the mode (most frequent value) of that column."""
app_score_col_rmvd['CNT_FAM_MEMBERS'] = \
    app_score_col_rmvd['CNT_FAM_MEMBERS'].fillna(app_score_col_rmvd['CNT_FAM_MEMBERS'].mode()[0])

print(app_score_col_rmvd['CNT_FAM_MEMBERS'].isnull().sum())

"""This line groups the data by the 'OCCUPATION_TYPE' column and calculates the size of each group 
(count of occurrences) for each unique occupation type, then sorts the results."""
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
"""This line provides summary statistics (e.g., mean, standard deviation) for the 'AMT_ANNUITY' column."""
print(app_score_col_rmvd['AMT_ANNUITY'].describe())
app_score_col_rmvd['AMT_ANNUITY'] = \
    app_score_col_rmvd['AMT_ANNUITY'].fillna((app_score_col_rmvd['AMT_ANNUITY'].mean()))
print(app_score_col_rmvd['AMT_ANNUITY'].isnull().sum())

# for amt_req_credit_bureau_hour
print(app_score_col_rmvd['AMT_REQ_CREDIT_BUREAU_HOUR'].describe())
print(app_score_col_rmvd['AMT_REQ_CREDIT_BUREAU_HOUR'].unique())

"""This code creates a list amt_req_col containing column names that start with "AMT_REQ_CREDIT_BUREAU."""
amt_req_col = []
"""These lines loop through the columns in amt_req_col and fill missing values in each of these columns with the median 
value of that respective column. It also prints the count of missing values for each column after the fill operation."""
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

"""These lines print the count of missing values in the 'AMT_GOODS_PRICE' column after the fill 
operation and also the mean value of that column.
"""
print(app_score_col_rmvd['AMT_GOODS_PRICE'].isnull().sum())
print(app_score_col_rmvd['AMT_GOODS_PRICE'].mean())

"""These lines print the first few rows of the app_score_col_rmvd DataFrame and the count
 of missing values in the 'AMT_CREDIT' column."""
print(app_score_col_rmvd.head())
print(app_score_col_rmvd['AMT_CREDIT'].isnull().sum())




