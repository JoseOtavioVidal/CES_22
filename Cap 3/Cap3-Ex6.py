#Import the library
import turtle

#Setup the screen
wn = turtle.Screen()
wn.title("Polygons")

#Create the turtle to draw a equilateral triangle
triangle = turtle.Turtle()
triangle.color("hotpink")
for i in range(3):
	triangle.forward(60)
	triangle.left(120)
	
#Create the turtle to draw a square
square = turtle.Turtle()
square.color("blue")
for i in range(4):
	square.forward(60)
	square.left(90)
	
#Create the turtle to draw a hexagon
hexagon = turtle.Turtle()
hexagon.color("red")
for i in range(6):
	hexagon.forward(60)
	hexagon.left(60)

#Create the turtle to draw a octagon
octagon = turtle.Turtle()
octagon.color("green")
for i in range(8):
	octagon.forward(60)
	octagon.left(45)
	
wn.mainloop()