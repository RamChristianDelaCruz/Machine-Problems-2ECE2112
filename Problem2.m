function problem2(p1,p2,p3)
syms x y
% x and y value of points
x1 = p1(1);
y1 = p1(2);
x2 = p2(1);
y2 = p2(2);
x3 = p3(1);
y3 = p3(2);
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
Equation = ((x-X)^2)+((y-Y)^2)== r^2;
expanded = expand(Equation);
%print the values asked%
fprintf("The radius is: %i \n",r)
fprintf("The center point is:(%i , %i) \n",X,Y)
fprintf("The General form is: ")
disp(expanded)