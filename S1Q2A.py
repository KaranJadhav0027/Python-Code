# Write a Python program to create a Pie plot to get the frequency of the three species of 
#the Iris data (Use iris.csv)
#S1Q2A.py
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
df

df['Species'].value_counts().plot.pie()
plt.title('Frequency of Three Species')
plt.legend()
plt.show()
