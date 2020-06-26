#CPSC 231
#Manjot Khangura
#Tutorial T02
#UCID: 30003843
#October 16, 2019
'''Program which draws an x-axis and y-axis with ticks within a set boundary of the turtle drawing library. The user inputs a mathematical expression
and the program will draw that expression, chaging colors from red, blue and green, as each new expression is being input. The program closes once a blank
("") expression is input'''

'''When inputting high exponential values (x**4 and higher) the program takes a long time to run it so  you will have to wait atleast a few minutes or
longer for the expression to be drawn and for the loop to start the next expression input.'''

#INFORMATION FOR YOUR TA

from math import *
import turtle

# CONSTANTS
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"

#
#  Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#
#  Parameters:
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x, y: the graph location to change into a screen (pixel-based) location
#
#  Usage -> screenCoor(xo, yo, ratio, 0, 0)
#
#  Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
#
def screenCoor(xo, yo, ratio, x, y):
    (screenX, screenY) = (((xo + (ratio * x)), (yo + (ratio * y)))) #Formula from the assignment 2 PDF, page #2
    return (screenX, screenY)

#
#  Returns a string of the colour to use for the current expression being drawn
#  This colour is chosen based on which how many expression have previously been drawn
#  The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
#  then loops back to red, then green, then blue, again
#
#  Usage -> getColor(counter)
#
#  Parameters:
#  counter: an integer where the value is a count (starting at 0) of the expressions drawn
#
#  Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.
#
def getColor(counter):
    if counter % 3 == 0:    #Draw a red line if the remainder of the value divided by 3 is 0
        return "red"
    if counter % 3 == 1:    #Draw a green line if the remainder of the value divided by 3 is 1
        return "green"
    else:                   #Draw a blue line otherwise
        return "blue"

#
#  Draw in the window an xaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  (screenX, screenY): the pixel screen location to draw the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawXAxisLabelTick(pointer, screenX, screenY, text):

    if text == 0:       #Condition so that the 0 text value is not written on the axes but all other values are
        pointer.up()    #Gets pointer off the screen
        pointer.goto(screenX, screenY)
        
#   Turtle pointer goes up 5 pixels from the screenY location and down 5 pixels from the screenY location. The pointer then gets off the screen and
#   then goes up then moves down 25 pixels from the screenY location before writing the text label.
    else:
        pointer.goto(screenX, screenY + 5) 
        pointer.goto(screenX, screenY - 5) 
        pointer.up()  
        pointer.goto (screenX, screenY - 25) 
        pointer.write(text, align = "center") 
        pointer.up() 
        pointer.goto(screenX, screenY)
    pass

#
#  Draw in the window an yaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawYAxisLabelTick(pointer, screenX, screenY, text):

    if text == 0:   #Condition so that the 0 text value is not written on the axes
        pointer.up()
        pointer.goto(screenX, screenY)
        
#   Turtle pointer goes right 5 pixels from the screenX location and left 5 pixels from the screenX location. The pointer then gets off the screen and
#   then goes up then moves left 15 pixels from the screenX location and down 8 pixels from screenY. The text value is then written.
    else:
        pointer.goto(screenX + 5, screenY)
        pointer.goto(screenX - 5, screenY)
        pointer.up()
        pointer.goto (screenX - 15, screenY - 8)
        pointer.write(text, align = "center")
        pointer.up()
        pointer.goto(screenX, screenY)
    pass

#
#  Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
#
#  Usage -> drawXAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: (xmin, xmax) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
#
def drawXAxis(pointer, xo, yo, ratio):
    x = 0       #Sets x as a local variable for the function
    y = 0       #Sets y as a local variable for the function
    text = 0    #Sets text as a local variable for the number for the x and y value under/beside the ticks
    HalfWidthNonPixel = (WIDTH / 2) / ratio #Variable for half of the x-axis (non-pixel location)
    (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
    pointer.up()
    pointer.goto(xo, yo)    #Go to origin

    while x <= HalfWidthNonPixel:           #Condition from x = 0 to the end of the turtle screen size on the right (positive end)
        (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(screenX, screenY)                      
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        x += 1              #Increments x value by 1
        text += 1           #Increments the text under ticks by 1
        if x <= HalfWidthNonPixel:          #Creates and updates xmax variable to x as long as it is within the upper x limits of the screen
            xmax = x
        else:
            xmax != x       
    x = 0                   #Resets x
    text = 0                #Resets text
    pointer.up()
    pointer.goto(xo, yo)    

    while x >= ((-1) * HalfWidthNonPixel):  #Condition from x = 0 to the end of the turtle screen size on the left (negative end)
        (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
        pointer.down()      #Gets pointer on the screen
        pointer.goto(screenX, screenY)                      
        drawXAxisLabelTick(pointer, screenX, screenY, text)
        x -= 1              #Increments x value by -1
        text -= 1           #Increments the text under ticks by -1
        if x >= ((-1) * HalfWidthNonPixel): #Creates and updates xmin variable to x as long as it is within the lower x limits of the screen
            xmin = x
        else:
            xmin != x
    
    return xmin, xmax

#
#  Draw in the window an yaxis
#
#  Usage -> drawYAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: Nothing
#
def drawYAxis(pointer, xo, yo, ratio):

#   Variables set the same way as drawXAxis function
    x = 0       
    y = 0       
    text = 0
    
    HalfHeightNonPixel = (HEIGHT / 2) / ratio   #Variable for half of the y-axis (non-pixel location)
    (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
    pointer.up()
    pointer.goto(xo, yo)

#   Condition from y = 0 to the end of the turtle screen size going up (positive end)
    while y <= HalfHeightNonPixel:
        (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(screenX, screenY)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        y += 1  #Increments y by 1
        text += 1

    y = 0       #Resets y back to 0
    text = 0
    pointer.up()
    pointer.goto(xo, yo)

#   Condition from y = 0 to the end of the turtle screen size going down (negative end)
    while y >= ((-1) * HalfHeightNonPixel): 
        (screenX, screenY) = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(screenX, screenY)
        drawYAxisLabelTick(pointer, screenX, screenY, text)
        y -= 1  #Increments y value by -1
        text -= 1
    pass

#
#  Draw in the window the given expression (expr) between [xmin, xmax] graph locations
#
#  Usage -> drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  expr: the expression to draw (assumed to be valid)
#  xmin, ymin : the range for which to draw the expression [xmin, xmax]
#
#  Returns: Nothing
#
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    
    #Draw expression
    x = xmin            #Start x as the xmin
    y = eval(expr)      #Allow y to evaluate the expression
    pointer.up()
    pointer.goto(screenCoor(xo, yo, ratio, x, y))
    pointer.down()

#   Condition where the graph is drawn from xmin all the way until xmax boundary
    while (x <= xmax and x >= xmin):
        y = eval(expr)
        x += 0.1        #Delta value of 0.1 to increment x in expr
        pointer.goto(screenCoor(xo, yo, ratio, x, y))
    pass

#
#  Setup of turtle screen before we draw
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer

#
#  Main function that attempts to graph a number of expressions entered by the user
#  The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
#  The window size is always 800 width by 600 height in pixels
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw experssions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1

#Run the program
main()
