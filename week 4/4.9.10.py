import turtle
window = turtle.Screen()
star = turtle.Turtle()

def draw_star(animal, length):
        for _ in range(6):
               animal.right(144)
               animal.forward(length)


draw_star(star, 150)
star.penup()
star.forward(50)
star.right(144)
star.pendown()
draw_star(star, 150)
star.penup()
star.forward(50)
star.right(144)
star.pendown()
draw_star(star, 150)
star.penup()
star.forward(50)
star.right(144)
star.pendown()
draw_star(star, 150)
star.penup()
star.forward(50)
star.right(144)
star.pendown()
draw_star(star, 150)
star.penup()
star.forward(350)
star.right(144)
star.pendown()

window.mainloop()