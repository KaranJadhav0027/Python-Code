#S2Q2A&B
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Data.csv")
df.head()

df['salary'].fillna(df['salary'].mean())

plt.plot(df['degree_t'], df['salary'])
plt.show() 
