#S1Q2B
#Write a Python program to view basic statistical details of the data.(Use wineequality-red.csv) 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv("wineQualityReds.csv")
data.head()

data.info()

data.describe()
