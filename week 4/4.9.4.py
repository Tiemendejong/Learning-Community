import turtle

def square(name):
   for _ in range(4):
       name.forward(200)
       name.left(90)


window = turtle.Screen()
aaa = turtle.Turtle()
window.bgcolor("lime green")
aaa.color("pink")
aaa.pensize(4)

for i in range(12):
    square(aaa)
    aaa.penup()
    aaa.forward(30)
    aaa.right(30)
    aaa.forward(30)
    aaa.pendown()
