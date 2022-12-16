import turtle
sc = turtle.Screen()
t = turtle.Turtle()

#D863F

#Drawing D
t.pencolor("Blue")
t.pensize(5)
t.left(90)
t.forward(100)
t.right(90)
t.circle(-50,180)

t.penup()
t.right(180)
t.forward(100)

t.pendown()

#drawing 8
t.circle(25)
t.penup()
t.goto(100,50)
t.pendown()
t.circle(25)

t.penup()
#drawing 6 left(kiri) | Rigth(kanan)
t.goto(150,0) #Position
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.right(180)
t.penup()
t.forward(50)
t.pendown()
t.forward(50)
t.right(90)
t.forward(50)

t.penup()
#Drawing 3
t.goto(230,0)
t.pendown()
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(25)
t.left(180)
t.penup()
t.forward(25)
t.pendown()
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(10)

#drawing F
t.penup()
t.goto(300,0)
t.pendown()
t.left(180)
t.forward(100)
t.right(90)
t.forward(50)
t.right(180)
t.penup()
t.forward(50)
t.pendown()
t.left(90)
t.penup()
t.forward(50)
t.pendown()
t.left(90)
t.forward(50)

t.penup()
t.goto(380,0)







sc.exitonclick()