import turtle
def koch(size,n):
    if n==0:
        turtle.fd(size)
    else:
        for angle in [0,60,-120,60]:
            turtle.left(angle)
            koch(size/3,n-1)
turtle.setup(800,400)
turtle.title('科赫曲线')
turtle.pensize(2)
turtle.penup()
turtle.goto(-300,-70)
turtle.pendown()
koch(600,3)
turtle.hideturtle()
turtle.done()
 