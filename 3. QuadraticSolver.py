#12.18.2017
#Quadratic Solver 2.4.6

'''Pseudocode: The program is designed to solve qudratics. It finds it's zeros and vertex.
It does this by asking the user for the 'a', 'b', and 'c' of the quadratic.
With these pieces of information, the program plugs in the variables into the quadratic formula and the formula to solve for the vertex.
It then ouputs the information solved for to the user.'''

import math

print('''Welcome to Quadratic Solver!
ax^2+bx+c
''')

def FindVertexPoint(A,B,C):
    if A > 0:
        x_vertex = (-B)/(2*A)
        y_vertex = (A*(x_vertex**2))+(B*x_vertex)+C
        return('Minimum Vertex Point: '+str(x_vertex)+', '+str(y_vertex))
    elif A < 0:
        x_vertex = (-B)/(2*A)
        y_vertex = (A*(x_vertex**2))+(B*x_vertex)+C
        return('Maximum Vertex Point: '+str(x_vertex)+', '+str(y_vertex))

def QuadraticFormula(A,B,C):
    D = (B**2)-(4*(A*C))
    if D < 0:
        return('No real solutions')
    elif D == 0:
        x = (-B+math.sqrt((B**2)-(4*(A*C))))/(2*A)
        return('One solution: '+str(x))
    else:
        x1 = (-B+math.sqrt((B**2)-(4*(A*C))))/(2*A)
        x2 = (-B-math.sqrt((B**2)-(4*(A*C))))/(2*A)
        return('Solutions: '+str(x1)+' or '+str(x2))
    
a = float(input("Quadratic's a: "))
b = float(input("Quadratic's b: "))
c = float(input("Quadratic's c: "))

print('')

print(QuadraticFormula(a,b,c))
print(FindVertexPoint(a,b,c))
