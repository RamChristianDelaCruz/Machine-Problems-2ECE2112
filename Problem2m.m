syms x y
% x and y value of points
x1 = input('Enter first point of X: ');
y1 = input('Enter first point of Y: ');
x2 = input('Enter second point of X: ');
y2 = input('Enter second point of Y: ');
x3 = input('Enter third point of X: ');
y3 = input('Enter third point of Y: ');
%midpoint of segments between 2 points %
MPx12 = (x1+x2)/2;
MPy12 = (y1+y2)/2;
MPx13 = (x1+x3)/2;
MPy13 = (y1+y3)/2;
%slope of segments%
Slope12 = (x2-x1)/(y2-y1);
Slope13 = (x3-x1)/(y3-y1);
%perpendicular slope%
PSlope12 = -1/(Slope12);
PSlope13 = -1/(Slope13);
%perpendicular bisector%
PB12 = y-(MPy12)-((PSlope12)*(x -MPx12));
PB13 = y-(MPy13)-((PSlope13)*(x -MPx13));
%Center point%
[X,Y] = solve(PB12,PB13);
%Radius of the circle%
r = sqrt(((X-x1)^2)+((Y-y1)^2));
%Equation of the circle%
Equation = ((x-X)^2)+((y-Y)^2) - r^2;
expanded = expand(Equation);
%print the values asked%
fprintf("The radius is: %i \n",r)
fprintf("The center point is:(%i , %i) \n",X,Y)
fprintf("The General form is: ")
disp(expanded)