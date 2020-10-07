import turtle

def square(aaa, corner, i):
     aaa.forward(i)
     aaa.right(corner)


window = turtle.Screen()
aaa = turtle.Turtle()
window.bgcolor("lime green")
aaa.color("blue")
aaa.pensize(4)


i = 5

for f in range(100):
    square(aaa, 88, i)
    i += 5

