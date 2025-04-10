#S30Q2B
from matplotlib import pyplot as plt
import numpy as np

cars = ['FDS', 'BLCOKCHAIN', 'TCS','SYSPRO', 'JAVA', 'INTERNET PROGRAMMING']
 
data = [23, 17, 35, 29, 12, 33]
 
# Creating plot
fig = plt.figure(figsize =(10, 7))
plt.pie(data, labels = cars)
 
# show plot
plt.show()
