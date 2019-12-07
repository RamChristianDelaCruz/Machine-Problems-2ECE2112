n = 0:99;
fofn = 0:99;
i = 0
while i ~=100
    x = i;
    i = i+1
   while x>=11
       x= x-10;
   end
   if x ==9
       x
       y(i) = NaN
       continue
   end
    fofn(i) = (x.^2)-7;
end
stem(n,fofn)
title('Machine Problem 1')
xlabel('n')
ylabel('f(n)')