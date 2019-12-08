import matplotlib.pyplot as plt
from sympy import symbols,solve
from math import *
formula=input('Enter Formula in terms of n: ')
n = symbols('n')
X = []
Y = []
xofn=0
yofn=0
for n in range(198):
    xofn=eval(formula)
    X.append(xofn)

for n in range(len(X)):
    if n==0:
        yofn= (-1.5*X[n]) + (2*X[n+1]) +(-0.5*X[n+2])
        Y.append(yofn)
    elif n>0 and n<197:
        yofn=0.5*(X[n+1]) -0.5*X[n-1]
        Y.append(yofn)
    else:
        yofn=1.5*X[n] -2*X[n-1] +0.5*X[n-2]
        Y.append(yofn)
N = []
for i in range(198):
    N.append(i)

plt.plot(N,X,label = 'X(n)')
plt.plot(N,Y,label ='Y(n)')
plt.title('Problem 5')
plt.legend(loc="upper right")


