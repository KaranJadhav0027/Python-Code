#S23Q2A&B&C
import numpy as np 
import pandas as pd 
from sklearn import preprocessing

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('wineQualityReds.csv')
df
col_names = list(df.columns)
col_names

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('Original Distributions')

sns.kdeplot(df['fixed.acidity'], ax=ax1)
sns.kdeplot(df['volatile.acidity'], ax=ax1)
sns.kdeplot(df['citric.acid'], ax=ax1)
sns.kdeplot(df['residual.sugar'], ax=ax1)
sns.kdeplot(df['chlorides'], ax=ax1);
sns.kdeplot(df['free.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df['total.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df['density'], ax=ax1);
sns.kdeplot(df['pH'], ax=ax1);
sns.kdeplot(df['sulphates'], ax=ax1);
sns.kdeplot(df['alcohol'], ax=ax1);
sns.kdeplot(df['quality'], ax=ax1);

mm_scaler = preprocessing.MinMaxScaler()
df_mm = mm_scaler.fit_transform(df)

df_mm = pd.DataFrame(df_mm, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After MinMaxScaler')

sns.kdeplot(df_mm['fixed.acidity'], ax=ax1)
sns.kdeplot(df_mm['volatile.acidity'], ax=ax1)
sns.kdeplot(df_mm['citric.acid'], ax=ax1)
sns.kdeplot(df_mm['residual.sugar'], ax=ax1)
sns.kdeplot(df_mm['chlorides'], ax=ax1);
sns.kdeplot(df_mm['free.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df_mm['total.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df_mm['density'], ax=ax1);
sns.kdeplot(df_mm['pH'], ax=ax1);
sns.kdeplot(df_mm['sulphates'], ax=ax1);
sns.kdeplot(df_mm['alcohol'], ax=ax1);
sns.kdeplot(df_mm['quality'], ax=ax1);


n_scaler = preprocessing.Normalizer()
df_n = n_scaler.fit_transform(df)

df_n = pd.DataFrame(df_n, columns=col_names)

fig, (ax1) = plt.subplots(ncols=1, figsize=(10, 8))
ax1.set_title('After Normalizer')

sns.kdeplot(df_n['fixed.acidity'], ax=ax1)
sns.kdeplot(df_n['volatile.acidity'], ax=ax1)
sns.kdeplot(df_n['citric.acid'], ax=ax1)
sns.kdeplot(df_n['residual.sugar'], ax=ax1)
sns.kdeplot(df_n['chlorides'], ax=ax1);
sns.kdeplot(df_n['free.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df_n['total.sulfur.dioxide'], ax=ax1);
sns.kdeplot(df_n['density'], ax=ax1);
sns.kdeplot(df_n['pH'], ax=ax1);
sns.kdeplot(df_n['sulphates'], ax=ax1);
sns.kdeplot(df_n['alcohol'], ax=ax1);
sns.kdeplot(df_n['quality'], ax=ax1);
