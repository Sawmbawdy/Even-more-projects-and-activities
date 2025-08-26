import turtle
turtle.Screen().bgcolor("white")
turtle.Screen().setup(800, 600)
turtle.title("Turtle's Spiral")
turtle.color("black")

t = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        t.fd(size + 1)
        t.left(90)
        size = size - 5
    size = size + 1