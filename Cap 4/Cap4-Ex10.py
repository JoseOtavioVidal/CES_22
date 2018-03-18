#Import the library
import turtle

#Create the fuction to draw a star
def draw_star(star, size):
	"Make a Star"
	for i in range(5):
		star.left(36)
		star.forward(size)
		star.left(108)
		
		
#Create the fuction to put the turtle in the right position
def position(star):
	for i in range (5):
		star.penup()
		star.forward(350)
		star.pendown()
		draw_star(star, 200)
		star.penup()
		star.forward(-350)
		star.right(144)

		
#Setup the screen
wn = turtle.Screen()
wn.title("Stars")
wn.bgcolor("lightgreen")
#Set up the turtle	
star = turtle.Turtle()
star.color("hotpink")
star.pensize(3)
#Call the fuction
position(star)
wn.mainloop()