import turtle

def round(t, n, sz):
   for _ in range(n):
       t.forward(sz)
       t.left(45)


window = turtle.Screen()
aad = turtle.Turtle()
window.bgcolor("lime green")
aad.color("pink")
aad.pensize(4)

round(aad, 8, 50)



