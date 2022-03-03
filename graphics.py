from pkggraphics.cirFunction import*
from pkggraphics.rectFunction import*
from pkggraphics.sphereFunction import*
l=int(input("enter length"))
b=int(input("enter bredth"))
print("area=",RectArea(l,b))
print("perimeter=",RecPerimeter(l,b))
r=int(int(input("enter the radius: ")))
print("cicle",CirArea(r))
r=int(input("enter radius of sphere"))
print("circle area =",SpArea(r))
print("circle perimeter=",SpPerimeter(r))
