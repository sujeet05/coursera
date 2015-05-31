# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explor


import simplegui
import math 



def project_to_distance(point_x ,point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)


def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))



def area(n,s):
    _rad= (math.pi)/n
    return (n * math.pow(s,2)) / (math.tan(_rad))

print area(5,7)/4
print "area"
print area(7,3)/4

_radians =math.radians(180)

print math.tan(_radians)
print math.tan(math.pi)    
def f(p,q):
    return not (p or not q)
print f(True,True)
print f(True,False)
print f(False,True)
print f(False,False)

def f(x):
    return -5*math.pow(x,5)+69*(math.pow(x,2))-47

print f(0)
print f(1)
print f(2)
print f(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value*(math.pow((1+rate_per_period),periods))

print "future value"
print future_value(500, .04, 10, 10)
print future_value(1000, .02, 365, 3)
message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
