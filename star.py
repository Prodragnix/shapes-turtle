import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
screen.bgcolor('Yellow')
pen.pencolor('Red')
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.penup()
pen.goto(0,60)
pen.pendown()
for _ in range(3):
    pen.forward(100)
    pen.right(120)

screen.mainloop()