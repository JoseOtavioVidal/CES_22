#Import the library
import turtle

#Setup the screen
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Clock")

#Create the turtle to draw a clock
clock = turtle.Turtle()
clock.color("blue")

#Setup the turtle
clock.shape("turtle")
clock.pensize(2)
angle = 30

#Start to draw
clock.stamp()
for i in range(12):
	clock.penup()
	clock.forward(120)
	clock.pendown()
	clock.forward(10)
	clock.penup()
	clock.forward(30)
	clock.stamp()
	clock.forward(-160)
	clock.left(angle)
	

wn.mainloop()