#S12Q2B
import pandas as pd
import numpy as np
data  = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
        'salary': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
        'dept': ['CS', 'MBA', 'CA', 'DOCTOR', 'CA', 'CS', 'CS', 'CS', 'MCA', 'ENG']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data , index=labels)
print(df)
df1 = df.dropna()

print(df1)
