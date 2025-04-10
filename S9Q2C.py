#S9Q2C
import pandas as pd
data = pd.read_csv("wineQualityReds.csv")
print("Shape of the data:")
print(data.shape)
print("\nData Type:")
print(type(data))
print("\nFirst 3 rows:")
print(data.head(3))
