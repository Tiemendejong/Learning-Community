import turtle
window = turtle.Screen()
dot = turtle.Turtle()
for i in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    dot.forward(100)
    dot.left(i)
    print(dot.pos())
window.mainloop()