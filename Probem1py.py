import matplotlib.pyplot as plt
fofn=[]
n=[]
i = 0
while i != 99:
    n.append(i)
    x=i
    i = i+1
    while x>=10:
        x=x-10
    if x<10:
        condition=(x**2)-7
        fofn.append(condition)
    else:
        continue
plt.title('Problem1')
plt.ylabel('f(n)')
plt.xlabel('n')
plt.stem(n,fofn)