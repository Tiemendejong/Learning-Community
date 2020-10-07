import turtle

def square(name, size):
   for _ in range(4):
       name.forward(size)
       name.left(90)


window = turtle.Screen()
tiemen = turtle.Turtle()
window.bgcolor("lime green")
tiemen.color("pink")

for i in range(5):
    square(tiemen, 20)
    tiemen.penup()
    tiemen.forward(40)
    tiemen.pendown()
