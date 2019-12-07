import matplotlib.pyplot as plt
import numpy as np
import math as m
X=[]
Y=[]
x=0
y=0
i=0
o=0
while i!=100:
    x=float(input('Enter X Value: '))
    x=int(x)
    X.append(x)
    response = str(input('Enter again? Y/N: '))
    if response == 'Y' or response == 'y':
        continue
    elif response == 'N' or response == 'n':
        break
    else:
        print('Type Y or N: ')
        
while i!=100:
    y=float(input('Enter Y Value: '))
    y=int(y)
    Y.append(y)
    response = str(input('Enter again? Y/N: '))
    if response == 'Y' or response == 'y':
        continue
    elif response == 'N' or response == 'n':
        break
    else:
        print('Type Y or N: ')

least=m.inf
for ctr in range(9):
    if ctr>=len(X):
        break
    p=np.polyfit(X,Y,ctr)
    Y2=np.polyval(p,X)
    e=Y-Y2
    errorvector_norm=np.linalg.norm(e)
    if errorvector_norm<least:
        least=errorvector_norm
        bestfit=p        
plt.title('Machine Problem: Problem 3')
Y3 = np.polyval(bestfit,X)
plt.plot(X,Y,'-o',label='Data points')
plt.plot(X,Y3,'-*',label='Best Fit')
plt.legend(loc="upper right")