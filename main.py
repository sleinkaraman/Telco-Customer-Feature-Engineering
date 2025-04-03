
##############################
# Telco Customer Feature Engineering
##############################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score,roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import warnings
warnings.simplefilter(action="ignore")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 170)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv("Telco-Customer-Churn.csv")

df.head()
df.shape
df.info()

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

df["Churn"] = df["Churn"].apply(lambda x : 1 if x == "Yes" else 0)


def check_df(dataframe, head=5):
    dataframe["TotalCharges"] = pd.to_numeric(dataframe["TotalCharges"], errors='coerce')

    print("SHAPE".center(70, "-"))
    print(dataframe.shape)

    print("TYPES".center(70, "-"))
    print(dataframe.dtypes)

    print("HEAD".center(70, "-"))
    print(dataframe.head(head))

    print("TAIL".center(70, "-"))
    print(dataframe.tail(head))

    print("MISSING VALUES".center(70, "-"))
    print(dataframe.isnull().sum())

    print("QUANTILES".center(70, "-"))
    print(dataframe.select_dtypes(include=['number']).quantile([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)
