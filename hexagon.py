import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
screen.bgcolor('#800000')
pen.pencolor('Black')
pen.fillcolor('Red')
pen.begin_fill()
for _ in range(6):
    pen.forward(100)
    pen.right(60)
pen.end_fill()

screen.mainloop()

