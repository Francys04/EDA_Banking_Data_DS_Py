from src.processing_prev_data import prev_app_nva_col_rmvd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.countplot(data=prev_app_nva_col_rmvd, x='NAME_CASH_LOAN_PURPOSE', hue='NAME_CONTRACT_STATUS')
plt.xticks(rotation=90)
plt.show()

