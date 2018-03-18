#Import the library
import turtle

#Create the fuction to draw a star
def draw_star(size):
	"""Make a Star"""
	star = turtle.Turtle()
	star.color("green")
	star.pensize(2)
	for i in range(5):
		star.left(36)
		star.forward(60)
		star.left(108)

		
#Setup the screen
wn = turtle.Screen()
wn.title("Star")
#Call the fuction
size = 100
draw_star(size)
wn.mainloop()