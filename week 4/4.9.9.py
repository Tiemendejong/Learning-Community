import turtle

def draw_star(animal, length):
    for _ in range(6):
        animal.right(144)
        animal.forward(length)

window = turtle.Screen()
star = turtle.Turtle()
draw_star(star, 150)

window.mainloop()