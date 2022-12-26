import turtle as t

tim = t.Turtle()
t.pensize(50)
# Turtle_1.shape("turtle")
# Turtle_1.color("red")

i = 3
while (i<10):
    j = 0
    while (j<i):
        tim.forward(100)
        tim.right(360/i)
        j += 1
    i += 1
    # tim.forward(4)
    # tim.penup
    # tim.forward(4)
    # tim.pendown


