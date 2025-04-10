#S26Q2A
import numpy as np

from matplotlib import pyplot as plt

X=np.random.randint(1,1000,50)
X

fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(X)
plt.show()

plt.plot(X) 
plt.show()

plt.scatter(X,X)
plt.show()

plt.boxplot(X)
plt.show()
