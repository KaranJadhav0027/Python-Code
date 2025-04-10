#S20Q2B
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

X=np.random.randint(1,1000,10)
X
df=pd.DataFrame(X , index=labels)
df

df.loc['d']=[11]
df

df.loc['h']=[79]
df

df.loc['ah']=[19]
df

df.rename(columns = {'0':'TEST'}, inplace = True)
df

sns.boxplot(data=df,x=df[0])
