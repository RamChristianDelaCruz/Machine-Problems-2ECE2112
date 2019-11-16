syms f n
%condition 1
n1 = [8:0.1:0];
f1 = (n1.^2)-7;
%condition 2
n2 = [10:0.1:99];
f2 = n2 - 10; %baka mali to

X = [f1,f2];
Y = [n1,n2];
%plotting
stem(f1,n1)
hold
grid on
stem(f2,n2)