import turtle

def square(name, size):
   for _ in range(4):
       name.forward(size)
       name.left(90)


window = turtle.Screen()
tiemen = turtle.Turtle()
window.bgcolor("lime green")
tiemen.color("pink")
tiemen.pensize(4)

size = 20
for a in range(5):
    square(tiemen, size)
    size += 20
    tiemen.penup()
    tiemen.right(90)
    tiemen.forward(10)
    tiemen.right(90)
    tiemen.forward(10)
    tiemen.left(180)
    tiemen.pendown()



