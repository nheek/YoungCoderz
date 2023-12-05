import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Hogwarts Logo")

# Set up the turtle
pen = turtle.Turtle()
pen.speed(3)  # Set the drawing speed

# Function to draw a circle with a given radius and color
def draw_circle(radius, color):
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw the Hogwarts logo
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Draw the outer circle
draw_circle(200, "gold")

# Draw the inner circles
circle_colors = ["red", "green", "blue"]
circle_radius = 160

for color in circle_colors:
    circle_radius -= 40
    draw_circle(circle_radius, color)

# Draw the horizontal line
pen.penup()
pen.goto(-200, 0)
pen.pendown()
pen.pensize(20)
pen.color("black")
pen.forward(400)

# Draw the vertical line
pen.penup()
pen.goto(0, 200)
pen.pendown()
pen.setheading(270)
pen.forward(180)

# Close the turtle graphics window when clicked
screen.exitonclick()
