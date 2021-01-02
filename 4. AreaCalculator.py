#1.5.2018
#Area Calculator 5.4.6

'''Pseudocode: The program is designed to calculate the area of multiple type of shapes.
It does this by asking the user for the shape of which they want to calculate the area of.
With this piece of information, the program asks the user for the necessary dimensions needed to calculate the area.
After plugging in the values inputed into the specific formula, it then ouputs the calculated area to the user.'''


print('''Welcome to Area Calculator!
      ''')

def AreaSquareOrRectangleOrParallelogram(l,w):
    A = l*w
    return A
def AreaTriangle(b,h):
    A = 0.5*b*h        
    return A
def AreaCircle(r):
    A = 3.14*(r**2)
    return A
def AreaTrapezoid(a,b,h):
    A = ((a+b)/2)*h
    return A
def AreaEllipse(a,b):
    A = 3.14*a*b
    return A

shape = input('Shape: ')
unit = input('Unit of Measurement: ')

if shape.lower() == 'square':
    side = float(input('Side: '))
    print(('Area:'),AreaSquareOrRectangleOrParallelogram(side,side), unit +('^2'))
elif shape.lower() == 'rectangle' or shape.lower() == 'parallelogram':
    length = float(input('Length: '))
    width = float(input('Width: '))
    print(('Area:'),AreaSquareOrRectangleOrParallelogram(length,width), unit +('^2'))
elif shape.lower() == 'triangle':
    base = float(input('Base: '))
    height = float(input('Height: '))
    print(('Area:'),AreaTriangle(base,height), unit +('^2'))
elif shape.lower() == 'circle':
    radius = float(input('Radius: '))
    print(('Area:'),AreaCircle(radius), unit +('^2'))
elif shape.lower()== 'trapezoid':
    base1 = float(input('Base 1: '))
    base2 = float(input('Base 2: '))
    height = float(input('Height: '))
    print(('Area:'),AreaTrapezoid(base1,base2,height), unit +('^2'))
elif shape.lower()== 'ellipse':
    axis1 = float(input('Axis 1: '))
    axis2 = float(input('Axis 2: '))
    print(('Area:'),AreaEllipse(axis1,axis2), unit +('^2'))
    
