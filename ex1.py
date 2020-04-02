from turtle import *

t = Turtle()
wn = Screen()

# Setting window standards
wn.bgcolor('#61cb6c')
wn.setup(width = 600, height = 600)
wn.title('Ex1')

# Setting turtle standards
t.color('#da54e6')
t.pensize(3)

for L in range(20, 20*5 + 1, 20):
    t.penup()
    t.goto(-L/2,-L/2)
    t.pendown()

    for i in range(4):
        t.forward(L)
        t.left(90)

t.penup()
t.goto(-20*6/2, -20*6/2)

done()
