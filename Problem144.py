from math import degrees, radians, tan, atan


def calc_line(p, q):
    """ Calculates the slope and intercept of the line which crosses points P and Q """
    m = (p[1]-q[1]) / (p[0]-q[0])
    n = p[1] - m*p[0]
    return m, n

def abc_formula(a, b, c):
    rad = (b**2-4*a*c)**0.5/(2*a)
    x1 = -b/(2*a) + rad
    x2 = -b/(2*a) - rad
    return x1, x2

def calc_intersection_line_elipse(m, n):
    x1, x2 = abc_formula(4+m**2, 2*m*n, n**2-100)
    y1 = m*x1 + n
    y2 = m*x2 + n
    return (x1, y1), (x2, y2)

print("stop")

def get_angle(m_old, m_tangent):
    arg = (m_old-m_tangent) / (1+m_old*m_tangent)
    return degrees(atan(arg))

def get_new_slope_from_angle(alpha, m):
    return (tan(radians(-alpha)) + m) / (1 - tan(radians(-alpha))*m)

def get_new_intercept(p, m):
    return p[1]-m*p[0]

def get_tangient_slope(x):
    return 4*x/((100-4*x**2)**0.5)

p = (0, 10.1)
q = (1.4, -9.6)
m, n = calc_line(p, q)
cnt=0
while True:   
    x1, x2 = abc_formula(4+m**2, 2*m*n, n**2-100)
    if abs(x1-p[0]) < 10**(-3):
        x = x2
    else:
        x = x1
    y = m*x+n
    if y>=0:
        m_tangent = -get_tangient_slope(x)
    else:
        m_tangent = get_tangient_slope(x)
    alpha = get_angle(m, m_tangent)
    m = get_new_slope_from_angle(alpha, m_tangent)
    p = (x, y)
    cnt+=1
    n = get_new_intercept(p, m)
    if -0.01 <= x and x <= 0.01 and y>0:
        break
print(cnt-1) # 354