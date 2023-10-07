from math import degrees, radians, tan, atan
from time import time

# TODO: Documentation + Time
""" The basis principle of the solution is to use the law: Angle of incidence equals angle of reflection """
start = time()

def calc_line(p, q):
    """ Calculates the slope and intercept of the line which crosses points P and Q """
    m = (p[1]-q[1]) / (p[0]-q[0])
    n = p[1] - m*p[0]
    return m, n

def abc_formula(a, b, c):
    """ Calculates the two solutions of a quadratic equation """
    rad = (b**2-4*a*c)**0.5/(2*a)
    x1 = -b/(2*a) + rad
    x2 = -b/(2*a) - rad
    return x1, x2

def calc_intersection_line_elipse(m, n):
    """ Calculates the two intersection points of a straight line and the given ellipse based on the intercept and slope of the line """
    x1, x2 = abc_formula(4+m**2, 2*m*n, n**2-100)
    y1 = m*x1 + n
    y2 = m*x2 + n
    return (x1, y1), (x2, y2)

def get_angle(m_old, m_tangent):
    """ Gets the angle between two lines given the slopes of the two lines """
    arg = (m_old-m_tangent) / (1+m_old*m_tangent)
    return degrees(atan(arg))

def get_new_slope_from_angle(alpha, m):
    """ Determines the slope of a third line, given the angle of the originally crossing lines and the slope of the line which is crossing with the 'new' line """
    return (tan(radians(-alpha)) + m) / (1 - tan(radians(-alpha))*m)

def get_new_intercept(p, m):
    """ Gets the new intercept, given the crossing point of the line with the ellipse and the slope of the line """
    return p[1]-m*p[0]

def get_tangient_slope(x):
    """ Get the slope of the tangient to the ellipse given the x-coordinate """
    return 4*x/((100-4*x**2)**0.5)

# Starting point when entering the ellipse
p = (0, 10.1)
# First point of reflection
q = (1.4, -9.6)
# Calculate the line between the two points
m, n = calc_line(p, q)
cnt=0
while True:
    # Get x coordinates of the two points the calculated line crosses the ellipse
    x1, x2 = abc_formula(4+m**2, 2*m*n, n**2-100)
    # If the intersection was already considered in the previous calculation, we need to consider the other one
    if abs(x1-p[0]) < 10**(-3):
        x = x2
    else:
        x = x1
    # Calculate the x coordinate
    y = m*x+n
    # We have to consider if we are at the lower or upper part of the ellipse because the solution of the quadratic equation is not unique (implicit function theorem) 
    if y>=0:
        m_tangent = -get_tangient_slope(x)
    else:
        m_tangent = get_tangient_slope(x)
    # Get the angle between the last straight line and the tangent
    alpha = get_angle(m, m_tangent)
    # Determine new slope from the angle based on law of reflection
    m = get_new_slope_from_angle(alpha, m_tangent)
    p = (x, y)
    n = get_new_intercept(p, m)
    # if we are at the opening of the ellipse, the laser beam can escape
    if -0.01 <= x and x <= 0.01 and y>0:
        break
    cnt+=1


print(cnt) # 354
print(f"Solution took {time()-start} seconds") # 0.040892839431762695 seconds