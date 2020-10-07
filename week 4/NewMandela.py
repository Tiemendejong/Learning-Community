import turtle
window = turtle.Screen()
window.bgcolor("pink")
mandela = turtle.Turtle()
mandela.color("blue")
mandela.speed(100)
def apple():
    mandela.penup()
    mandela.left(25)
    mandela.forward(25)
    mandela.pendown()

def samsung():
    mandela.forward(50)
    mandela.left(45)

for i in range(28):
    apple()
    for j in range(8):
           samsung()

window.mainloop()
#Is it more readable?