#S16Q2B
import pandas as pd
data  = {'name': ['ABC', 'DEF', 'KLM', 'JKL', 'EFG', 'MNO', 'MMMM', 'LMNO', 'PQQR', 'XYZ'],
        'percentage': [65, 59, 75, 59.63, 89, 72, 64.5, 71, 87, 81],
        'age': [17,19,20,19,19,18,19,17,18,20]}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data , index=labels)
df
avg=sum(df['percentage'])/len(df['percentage'])
print("Average of Percentages :",avg)
avg=sum(df['age'])/len(df['age'])
print("Average of age :",avg)
