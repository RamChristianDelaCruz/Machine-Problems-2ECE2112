import matplotlib.pyplot as plt
import numpy as np
import math as m
X=np.array([])
Y=np.array([])
x=0
y=0
i=0
o=0
#User input
while i!=1:
    x=float(input('Enter X Value: '))
    x=(x)
    X=np.append(X,x)
    y=float(input('Enter Y Value: '))
    y=(y)
    Y= np.append(Y,y)
    response = str(input('Enter again? Y/N: '))
    if response == 'Y' or response == 'y':
        continue
    elif response == 'N' or response == 'n':
        break
    else:
        print('Type Y or N: ')
#array of data points        
N = np.column_stack((X,Y))
#approximation
LeastNorm=m.inf
for degree in range(9):
    if degree>=len(X):
        break
    P1=np.polyfit(X,Y,degree)
    Y2=np.polyval(P1,X)
#Plotting
plt.title('Problem 3')
plt.plot(X,Y, 'o', color='black',markersize=15,label='Data Points')
plt.plot(X,Y2,'--h',label='Approximated')
plt.legend(loc="upper right")