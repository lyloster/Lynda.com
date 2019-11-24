import turtle

#creates a drawing screen
screen = turtle.Screen()

#background color
screen.bgcolor("blue") 
screen.title("Draw Lines Practice")

#creates a turtle
myTurtle = turtle.Turtle()
#line thickness
myTurtle.pensize(5)
#shape of pen
myTurtle.shape("circle")
#number of pixels
myTurtle.forward(100)
#degrees
myTurtle.left(45)
# lift without drawing
myTurtle.penup()
myTurtle.forward(100)
myTurtle.pendown()
myTurtle.forward(100)
myTurtle.backward(100)

#window stays open
#needs to be after creating the window, otherwise blank
# screen and turtle equivalent?
#calls mainloop() from file turtle
#screen is of type turtle, maybe that's why it works with both
screen.mainloop()