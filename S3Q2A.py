#S3Q2A
import pandas as pd
from sklearn import datasets
import seaborn as sns

df = pd.read_csv('Iris.csv')
df

sns.boxplot(x="Species", y="PetalLengthCm", data=df )
plot.show()

sns.boxplot(x="Species", y="SepalWidthCm", data=df )
plot.show()

sns.boxplot(x="Species", y="PetalLengthCm", data=df )
plot.show()

sns.boxplot(x="Species", y="PetalWidthCm", data=df )
plot.show()
