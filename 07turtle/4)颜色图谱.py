import turtle as t
t.colormode(255)
colors=["red","orangered","orange",(253,198,11),"yellow","yellowgreen","green"
        ,(6,150,187),"blue",(68,78,153),"Purple",(196,3,125)]
x=t.xcor()
for i in colors:
    t.color(i)
    t.begin_fill()
    for j in range(4):
        t.forward(50)
        t.left(90)
    t.end_fill()
    t.penup()
    x+=60
    t.goto(x,0)
    t.pendown()
t.done()