from src.processing import flag_tgt_col, flag_col, corr_df, app_flag_rmvd
from src.processing import app_score_col_rmvd
from src.config import app
import seaborn as sns
import matplotlib.pyplot as plt

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


