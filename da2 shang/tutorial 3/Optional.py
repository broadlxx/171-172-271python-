import turtle


def drawtree(n,t):
    t.pd()
    if n<5:
        return
    elif n<10:
        t.color("darkgreen")
        t.pensize(1)
    elif n<100:
        t.color("brown")
        t.pensize(2)
    else:
        t.color("black")
        t.pensize(3)

alex = turtle.Turtle()
# make alex look like a turtle
alex.shape("turtle")

# another new turtle
tess = turtle.Turtle()
# set pen color and thickness for tess
tess.color("hotpink")
tess.pensize(3)

# pick pen up off paper
tess.penup() or tess.pu()

# put pen down to draw
tess.pendown() or tess.pd()

# go to starting point, middle of screen = (0,0)
alex.goto(0,-200)

# turn right 90 degrees
alex.right(90)

# make alex invisible
alex.hideturtle()

# put pen down to draw
alex.pd()

# go forward 20 steps
alex.forward(20)
# put pen down to draw
tess.pendown()


