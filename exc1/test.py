import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('ex1data1.txt', header=None,names=['Population','profit'])
X=data['Population']
Y=data['profit']
N=len(X)

plt.scatter(X,Y,c='r',marker='*',s=50)
plt.xlabel('Population')
plt.ylabel('Profit')
plt.title('Population vs Profit')

# plt.show()
