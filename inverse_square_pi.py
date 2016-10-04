"""
Approximation of Pi, using a method similar to Archimedian "method of exhaustion."

Archimedes of Syracuse, in Sicily, (287-212 BCE) used a method of approximating the area of the unit circle using inscribed and circumscribed polygons,
this is also known as the classical method of exhaustion.

Archimedes stated that the area (by extension we consider the CIRCUMFERENCE) of a regular n-sided polygon inscribed in an arbitrarily sized circle is less than the actual area of the circle.
As n approaches infinity, the two polygonal areas should approach the area of the unit circle -- and by extension, the circumference should approximate an ideal circle.

This approach is slightly cheating because we are leveraging Python's "math" library and exploiting sin(x) and cos(x) to find the ENDPOINT of a Vector originating at 
Cartesian coordinates of 0,0.

The next exercise will be to use a simulated annealing approach to finding the polygonal endpoints that will lie on the unit circle.
This should, in-effect, remove the dependency on the math library's trignometric functions.
"""
import math
import os

class Point(object):
    x = 0.0
    y = 0.0
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
        
    def distance(self,point):
        return math.sqrt((point.x-self.x)**2+(point.y-self.y)**2)
    
    def __str__(self):
        return "({},{})".format(self.x,self.y)

class Vector(object):
    '''A Vector is an abstract 2 dimensional path that has a magnitude and direction
    The magnitude is unitless, the direction is specified in either degrees or radians
    but internally represented as radians'''
    
    magnitude = 0.0
    direction = 0.0
    
    def __init__(self, magnitude, direction, degrees=True):
        self.magnitude = magnitude
        self.direction = direction
        if degrees:
            # overide if degrees are specified or not supplied by user
            self.direction = math.radians(direction)
        
    def cartesian(self,origin=Point(0,0)):
        '''return the cartesian coordinates of the vector tip based on a Point origin'''
        return Point(self.magnitude*math.cos(self.direction),
                self.magnitude*math.sin(self.direction))
        
        
def approximate_circumference_of_polygon(sides, radius=1.0):
    poly = [] # an empty list which contains the vertices of a polygon
    sides = sides / 4 # only going to consider the first quadrant
    dd = 90.0/sides # we are only working in the first quadrant (or 90 degrees) of the circle
    
    for s in range(0,sides+1):
        direction = s * dd
        v = Vector(magnitude=radius,direction=direction)
        poly.append(v.cartesian())
    
    if DEBUG:
        for p in poly:
            print p
        
    # calculate circumference of the polygon
    c = 0.0
    for i in range(0,len(poly)-1):
        c += poly[i].distance(poly[i+1])
    
    my_pi = c*2/radius
    print "Approximation of circumference = ", c * 4
    print "Radius of circle = ", radius
    print "Approximation of pi = ", my_pi
    
    print "Difference of approximate pi and math library reference value = ", abs(math.pi-my_pi)
    
    return c*4
    
user_input_required = True
exit_program = False
DEBUG = False

while user_input_required:
    print "Calculating pi by creating an N-sided polygon and finding its circumference"
    sides = raw_input("How many sides? (must be divisible by 4) or ENTER to quit: ")
    if sides != '':
        try:
            sides = int(sides)
            if sides == 0:
                exit_program = True
            if sides > 0 and sides % 4 == 0:
                user_input_required = False
        except:
            pass
        
        if user_input_required:
            print "Try again."
        else:
            c = approximate_circumference_of_polygon(sides)
            user_input_required = True

    else:
        user_input_required = False # exit the program
    
    
    
    
    

