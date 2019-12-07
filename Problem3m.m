x=[];
y=[];
i =0;
%User input%
while i<1
    xval=input('Enter X Value: ')
    x(end+1) = xval
    yval=input('Enter y Value: ')
    y(end+1) = yval
    
    response = input('Enter again? 1/2: ')
    if response == 1
        continue
    elseif response == 2
        break
    else
        fprintf('Type Y or N \n')
        continue
    end 

end
leastnorm = inf;
for degree=1:1:10
    if degree>=length(x)
        continue
    end
    P1 = polyfit(x,y,degree)
    P2 = polyval(P1,x); 
    error = y-P2;
    NormOfErrorVector = norm(error)
    if NormOfErrorVector < leastnorm
        leastnorm = NormOfErrorVector
        plot(x,y,'ko','markersize',15)
        hold on;
        plot(x,P2,'--h')
        hold off;
        title('Problem 3')
        legend('Data Points','Approximated')
    end
end
