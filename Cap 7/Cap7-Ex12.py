#Import the library
import turtle
import math

#Create the fuction to draw a house
def draw_house(movement):
	"""Make a house using the commands of the list"""
	alex = turtle.Turtle()
	alex.color("green")
	alex.pensize(2)
	for (angle, lenght) in movement:
		alex.left(angle)
		alex.forward(lenght)

		
#Setup the screen
wn = turtle.Screen()
wn.title("House")
#Setup the list of pairs
movement = [(0, 50), (90, 50), (90, 50), (90, 50),(135, 50*math.sqrt(2)), (75, 50), (120, 50), (75, 50*math.sqrt(2))]
print(type(movement))
#Call the fuction
draw_house(movement)
wn.mainloop()