#Import the library
import turtle
import math

# We can only draw a picture without lifting the pen or going over an edge more than once if the picture have
# , in maximum, a pair of vertices with a odd degree

#Create the fuction to draw the picture
def draw_picture(movement):
	"""Make a picture using the commands of the list in the tuple"""
	alex = turtle.Turtle()
	alex.color("green")
	alex.pensize(2)
	for (angle, lenght) in movement:
		alex.left(angle)
		alex.forward(lenght)

		
#Setup the screen
wn = turtle.Screen()
wn.title("Pictures")
#Setup the list of pairs
movement = [(0, 50), (90, 50), (90, 50), (90, 50),(135, 50*math.sqrt(2)), (75, 50), (120, 50), (75, 50*math.sqrt(2))]
movement1 = 
print(type(movement))
#Call the fuction
draw_house(movement)
wn.mainloop()