#CPSC 231
#Manjot Khangura
#Tutorial T02
#UCID: 30003843
#September 27, 2019
'''
Assignment 1: I make a graph where I ask the user for input on coordinates on a circle and a line in which the program will draw the circle and line and
then indicate any intersections with a green circle or indicate that there are no intersections.
'''

def DrawTheAxis(): #Function to draw the x and y axis
    pointer.penup() #Pick up the turtle pen off the screen
    pointer.setpos(0, MIDDLEY) #Positions to (0, 300)
    pointer.pendown() #Put the pen back down on the screen
    pointer.goto(WIDTH, MIDDLEY) #Makes x-axis
    pointer.penup()
    pointer.setpos(MIDDLEX, 0) #Positions to (400, 0)
    pointer.pendown()
    pointer.goto(MIDDLEX, HEIGHT) #Makes y-axis

def DrawTheCircle(): #Function to draw the circle form the input
    pointer.penup()
    pointer.setpos(xCircle, yCircle-cRadius) #Sets to the middle coordinates of the circle
    pointer.pendown()
    pointer.circle(cRadius) #Draws the circle

def DrawTheLine(): #Function to draw the line from the input
    pointer.penup()
    pointer.home()
    pointer.setpos(xLine1, yLine1) #Sets pointer to start of line
    pointer.pendown()
    pointer.goto(xLine2, yLine2) #Draws pointer to the end of the line

def SetPointerToMiddle(): #Function to set pointer to (400,300) coordinate
    pointer.penup()
    pointer.setpos(MIDDLEX, MIDDLEY)
    pointer.pendown()

def WriteNoIntersects(): #Gives no intersections statement
    pointer.write('No Intersect!', align='center')
    print('There are no intersects!')

def WriteOneIntersect(): #Gives one intersection statement
    print('There is 1 intersect!')
    
def WriteTwoIntersects(): #Gives two intersections statement
    print('There are 2 intersects!')

def Alpha1Intersection(): #Draws circle around Alpha1 intersection
    pointer.penup()
    pointer.setpos(xIntersect1, yIntersect1 - IntersectionRadius)
    pointer.pendown()
    pointer.circle(IntersectionRadius)

def Alpha2Intersection(): #Draws circle around Alpha2 intersection
    pointer.penup()
    pointer.setpos(xIntersect2, yIntersect2 - IntersectionRadius)
    pointer.pendown()
    pointer.circle(IntersectionRadius)

#Import the libraries
import turtle
import math

WIDTH = 800
HEIGHT = 600
MIDDLEX = WIDTH / 2
MIDDLEY = HEIGHT / 2

'''
Setup the world (get the objects, set the screen size and coordinate system,
hide the pointer, and speed up turtle drawing)
'''
pointer=turtle.Turtle()
screen=turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()
pointer.speed(0)

pointer.pencolor('black') #Change pointer pen color

DrawTheAxis() #Function for the axis

pointer.pencolor('red')

AllowLoop = True #Boolean to close the second while loop for line inputs is the circle input while loop is false

while True: #While loop for circle inputs using a catch statement to prevent errors if wrong input is put in

    try:
        #User input on circle coordinates and radius
        xCircle = int(input('Please enter the x coordinate of the centre of the circle: '))
        yCircle = int(input('Please enter the y coordinate of the circle: '))
        cRadius = float(input('Please enter the radius of the circle: '))
        DrawTheCircle()
    except (ValueError, EOFError): #Bypass value and EOF error
        print('\nYour response is invalid, program will close on click...')
        AllowLoop = False #If there is an error, the AllowLoop boolean becomes false
    break

CountIntersections = 0 #Global variable for accumulation of intersections for while loop in print statements at the end

'''
While loop for circle inputs using a catch statement to prevent errors if wrong input is put in. Also it loops more inputs continuously until the wrong
input is put in.
'''
while True:

    if not AllowLoop: #If the circle while loop is false from the boolean (AllowLoop) being false, this line input while loop will break automatically
        break
        turtle.exitonclick()
    elif AllowLoop:
        pointer.pencolor('blue')
        try:
            #User input on line coordinates (start and end)
            xLine1 = int(input('Please enter the x coordinate of the start of the line: '))
            yLine1 = int(input('Please enter the y coordinate of the start of the line: '))
            xLine2 = int(input('Please enter the x coordinate of the end of the line: '))
            yLine2 = int(input('Please enter the y coordinate of the end of the line: '))
            DrawTheLine()
        except (ValueError, EOFError): #bypass value and EOF errors
            print('\nYour response is invalid, program will close on click...')
            break
            turtle.exitonclick()

        pointer.pencolor('green')

        #Variables for the quadratic formula
        a = ((xLine2 - xLine1) ** 2) + ((yLine2 - yLine1) ** 2)
        b = 2 * (((xLine1 - xCircle) * (xLine2 - xLine1)) + ((yLine1 - yCircle) * (yLine2 - yLine1)))
        c = ((xLine1 - xCircle) ** 2) + ((yLine1 - yCircle) ** 2) - ((cRadius) ** 2)
        d = ((b ** 2) - (4 * a * c)) #Variable for value under the square root

        IntersectionRadius = 5 #Radius of circle to be drawn around intersections

        if d < 0: #Condition where d variable less than 0
            
            SetPointerToMiddle()
            WriteNoIntersects()
            CountIntersections+=0 #Doesn't add an intersection to the print statements at the end
            
        elif d == 0: #Condition where d variable equals 0

            #Quadratic formula for Alpha1 intersection
            Alpha1 = (((-1) * b) + (math.sqrt(d))) / (2 * a)
            Alpha2 = (((-1) * b) - (math.sqrt(d))) / (2 * a)
            #Formulas for Alpha1 intersect
            xIntersect1 = (1 - Alpha1) * (xLine1) + (Alpha1 * xLine2)
            yIntersect1 = (1 - Alpha1) * (yLine1) + (Alpha1 * yLine2)
            xIntersect2 = (1 - Alpha2) * (xLine1) + (Alpha2 * xLine2)
            yIntersect2 = (1 - Alpha2) * (yLine1) + (Alpha2 * yLine2)
            
            Alpha1Intersection()
            SetPointerToMiddle()
            WriteOneIntersect()
            CountIntersections+=1 #Adds one more intersection to print statements at the end

        else: #Sets conditions for intersections within an Alpha boundary of 0 to 1 and also outside it

            #Quadratic formula for intersections
            Alpha1 = (((-1) * b) + (math.sqrt(d))) / (2 * a)
            Alpha2 = (((-1) * b) - (math.sqrt(d))) / (2 * a)
            
            #Formulas for Alpha intersects
            xIntersect1 = (1 - Alpha1) * (xLine1) + (Alpha1 * xLine2)
            yIntersect1 = (1 - Alpha1) * (yLine1) + (Alpha1 * yLine2)
            xIntersect2 = (1 - Alpha2) * (xLine1) + (Alpha2 * xLine2)
            yIntersect2 = (1 - Alpha2) * (yLine1) + (Alpha2 * yLine2)

            #Condition where Alpha1 intersection has a circle drawn around it
            if Alpha1 >= 0 and Alpha1 <= 1: #Alpha1 condition between 0 and 1
                Alpha1Intersection()
                
            #Condition where Alpha2 intersection has a circle drawn around it
            if Alpha2 >= 0 and Alpha2 <= 1: #Alpha2 condition between 0 and 1
                Alpha2Intersection()

            #Alpha1 and Alpha2 print and write conditions outside the 0 and 1 boundary
            if (Alpha1 <= 0 or Alpha1 >= 1) and (Alpha2 <=0 or Alpha2>=1): 
                SetPointerToMiddle()
                WriteNoIntersects()
                CountIntersections+=0

            #Print condition where Alpha1 is not in the boundary but Alpha2 is
            elif (Alpha1 <= 0 or Alpha1 >= 1) and not (Alpha2 <= 0 or Alpha2 >= 1):
                SetPointerToMiddle()
                WriteOneIntersect()
                CountIntersections += 1

            #Print condition where Alpha2 is not in the boundary but Alpha1 is
            elif (Alpha2 <= 0 or Alpha2 >= 1) and not (Alpha1 <= 0 or Alpha1 >= 1):
                SetPointerToMiddle()
                WriteOneIntersect()
                CountIntersections += 1
                
            #Print condition where both Alpha values are in the boundary
            else:
                SetPointerToMiddle()
                WriteTwoIntersects()
                CountIntersections += 2 #Adds two intersections to the print statements at the end

        #Conditional statments for the print statements which accumulate the number of intersections for the while loop
        if d < 0:
            print('There is a total of',CountIntersections,'intersection(s)!')
                
        elif d == 0:
            
            print('There is a total of',CountIntersections,'intersection(s)!')

        else:
            #Quadratic formula for Alpha1 intersection
            Alpha1 = (((-1) * b) + (math.sqrt(d))) / (2 * a)
            Alpha2 = (((-1) * b) - (math.sqrt(d))) / (2 * a)
            
            #Formulas for Alpha1 intersect
            xIntersect1 = (1 - Alpha1) * (xLine1) + (Alpha1 * xLine2)
            yIntersect1 = (1 - Alpha1) * (yLine1) + (Alpha1 * yLine2)
            xIntersect2 = (1 - Alpha2) * (xLine1) + (Alpha2 * xLine2)
            yIntersect2 = (1 - Alpha2) * (yLine1) + (Alpha2 * yLine2)
            
            #If statements that will accumulate intersections in print statements based on the condition
            if (Alpha1 <= 0 or Alpha1 >= 1) and not (Alpha2 <= 0 or Alpha2 >= 1):
                print('There is a total of',CountIntersections,'intersection(s)!')

            elif (Alpha2 <= 0 or Alpha2 >= 1) and not (Alpha1 <= 0 or Alpha1 >= 1):
                print('There is a total of',CountIntersections,'intersection(s)!')

            else:
                print('There is a total of',CountIntersections,'intersection(s)!')
            
#Exits turtle with a click
turtle.exitonclick()
