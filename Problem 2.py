from sympy import symbols,solve
from math import sqrt 
x = symbols('X')
y = symbols('Y')
# x and y value of points
x1 = float(input('Input first point of x: '))
y1 = float(input('Input first point of y: '))
x2 = float(input('Input second point of x: '))
y2 = float(input('Input second point of y: '))
x3 = float(input('Input third point of x: '))
y3 = float(input('Input third point of y: '))
# midpoint of segments between two points
MPx12 = (x1+x2)/2
MPy12 = (y1+y2)/2
MPx13 = (x1+x3)/2
MPy13 = (y1+y3)/2
#slope of segments
Slope12 = (x2-x1)/(y2-y1)
Slope13 = (x3-x1)/(y3-y1)
#perpendicular slope
PSlope12 = -1/(Slope12)
PSlope13 = -1/(Slope13)
#perpendicular bisector
PB12 = y-(MPy12)-((PSlope12)*(x -MPx12))
PB13 = y-(MPy13)-((PSlope13)*(x -MPx13))
#Center point
CP = solve((PB12,PB13),(x,y))
X = CP[x]
Y = CP[y]
#Radius of the circle
r = sqrt(((X-x1)**2)+((Y-y1)**2))
#Equation of the circle
Equation = ((x-X)**2)+((y-Y)**2)+ r**2

print('The radius is: ',round(r,2))
print('The center point is: ',round(X,2),round(Y,2))
print('The equation is: ',Equation)
