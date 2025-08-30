import turtle
pi = 3.14
def findcircumference(Rad):
    circumference = 2 * pi * int(Rad)
    return circumference
Radius = int(input("Enter the radius of the circle: "))

print("The circumference of the circle is:", findcircumference(Radius))
turtle.Screen().bgcolor("lightblue")
turtle.Screen().title("Circle with Circumference")
turtle.Screen().setup(width=600, height=600)
t = turtle.Turtle()
t.speed("fastest")
t.hideturtle()
t.color("black")
t.speed(1)
turtle.circle(Radius*10)
t.penup()
t.goto(0, -100)
t.pendown()
t.visible = False
t.write(f"Circumference: {findcircumference(Radius)}", align="center", font=("Arial", 16, "normal"))
turtle.done()
