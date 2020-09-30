import turtle
window = turtle.Screen()
window.bgcolor("pink")
mandela = turtle.Turtle()
mandela.color("blue")
mandela.speed(100)
for i in range(28):
    mandela.penup()
    mandela.left(25)
    mandela.forward(25)
    mandela.pendown()
    for j in range(8):
           mandela.forward(50)
           mandela.left(45)
window.mainloop()