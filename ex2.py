from turtle import *
from math import *

def draw_poly (t, n, sz):
    t.penup()

    angle = 360/n

    x = -sz/2
    y = -sz/(2*tan(angle*pi/360))
    t.goto(x,y)

    t.pendown()
    for i in range(n):
        t.forward(sz)
        t.left(angle)

# Demonstration
def main ():
    t = Turtle()
    wn = Screen()

    # Setting window standards
    wn.bgcolor('#61cb6c')
    wn.setup(width = 600, height = 600)
    wn.title('Ex1')

    # Setting turtle standards
    t.color('#da54e6')
    t.pensize(3)

    for i in range(10):
        draw_poly(t, 4 + i, 50 + 10*i)

    done()

if __name__ == '__main__':
    main()
