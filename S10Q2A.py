#S10Q2A
import pandas as pd
df = pd.read_csv('HeightWeight.csv')
print(df)
m1=df['Height'].mean()
m2 = df['Weight'].mean()
med1 = df['Height'].median()
med2 = df['Weight'].median()
print('mean of Height: ' + str(m1))
print('mean of Weight: ' + str(m1))
print('Median of Height: ' + str(med1))
print('Median of Weight: ' + str(med2))

