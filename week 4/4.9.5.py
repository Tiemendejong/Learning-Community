import turtle

def square(name, corner, i):
       name.forward(i)
       name.right(corner)


window = turtle.Screen()
aaa = turtle.Turtle()
window.bgcolor("lime green")
aaa.color("blue")
aaa.pensize(4)


i = 5 

for f in range(100):
    square(aaa, 90, i)
    i += 5
