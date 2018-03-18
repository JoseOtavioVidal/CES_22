import turtle

#Setup the screen
wn = turtle.Screen()
wn.title("Star")

#Create the turtle to draw a star
star = turtle.Turtle()
star.color("green")
star.pensize(2)
for i in range(5):
	star.left(36)
	star.forward(60)
	star.left(108)
	
wn.mainloop()