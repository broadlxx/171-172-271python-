import	turtle
wn	=	turtle.Screen()
my_turtle	=	turtle.Turtle()
for i in range(0,101,10):
    my_turtle.forward(i)
    my_turtle.left(90)
    my_turtle.forward(i)
    my_turtle.left(90)
wn.exitonclick()
