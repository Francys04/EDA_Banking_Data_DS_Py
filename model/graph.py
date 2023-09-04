from src.processing import flag_tgt_col, flag_col, corr_df, app_flag_rmvd  # It might be used for analyzing the
# relationship between various flags and the target variable.
# This could be a list of column names related to flags or binary indicators in a dataset, used for further analysis.
from src.processing import app_score_col_rmvd  # This DataFrame seems to be the result of some processing or feature
# engineering applied to another dataset, possibly app. It might contain specific columns related to scores or
# other features.
from src.config import app
import seaborn as sns
import matplotlib.pyplot as plt

"""
These lines create subplots within the figure to display count plots for different columns specified in flag_col. 
It iterates through flag_col using enumerate, and for each column (col), it creates a subplot using plt.subplot. 
The count plots are created using sns.countplot, and the hue parameter is used to distinguish counts based on the 
'TARGET' variable.
"""
# how it works
plt.figure(figsize=(20, 20))
for i, col in enumerate(flag_col):
    plt.subplot(7, 4, i + 1)
    sns.countplot(data=flag_tgt_col, x=col, hue='TARGET')
plt.show()

'''Show the graphic result of some data of FLAGS ...'''
plt.figure(figsize=(10, 5))
sns.heatmap(corr_df, cmap='coolwarm', linewidths=.5, annot=True)

sns.heatmap(data=round(app_flag_rmvd[['EXT_SOURCE_2', 'EXT_SOURCE_3']].corr(), 2), cmap='coolwarm',
            linewidths=.5, annot=True)


