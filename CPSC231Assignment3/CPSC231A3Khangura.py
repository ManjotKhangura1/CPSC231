#CPSC 231
#Manjot Khangura
#Tutorial T02
#UCID: 30003843
#November 15, 2019
'''Program that handles arguments where either the user puts a star ;ocation file in the arguments or it is prompted to the user. The
program will then take the star file (if they are valid, else the system will exit) and plot it using a list of the star coordinates
(x, y, and magnitude of the stars) in grey and then make a dictionary for the named stars and plot them in white. The user is then
prompted to give a constellation file and if it is a valid file, the program looks at the names in that file and uses the returned
dictionary to find the names which are keys in the dictionary and it draws lines and makes the constellation. After the constellation
is made, a bounding box is drawing around the constellation with the constellations name written above it. A .dat file is also made for
the constellation where its xmin, xmax, ymin, and ymax values are stored. Finally, the user is continually prompted for constellation 
files until they hit enter.'''

# Some comments are almost identical to assignment 2 because the functions were almost the same when used in this assignment

# Import appropriate libraries
import sys
import os
import turtle

# Constants for the setup of turtle and the colors which the pointer will use for drawing as well as the background color
WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"
# Constants for axis drawing because the origin and ratio is not going to change
XO = 300
YO = 300
RATIO = 300
# Increment x-axis and y-axis in drawXaXis and drawYAxis functions
INCREMENT = 0.25
PADDING = 15
PADDINGCOLOR = "orange"
# Moves pointer up or down from screenX and screenY when making ticks on axes
LABELTICK = 5
# Moves pointer slightly away from ticks to make room to write axes numbers
WRITETEXT = 25

# Handles command line arguments
# Arguments are of length 1 to 3 where anything more exits the program
# if the specific index of an argument isn't what is needed according to the assignment, the system exits
# If the star_location_file is not valid or isn not found, the system exits
# Parameters: None
# Usage: handleArguments()
# Returns:
#   stars_location_file: The star file that the user either puts in an arguments or is prompted to put in (if it is a valid file)
#   nameCheck: A sboolean that will return True is "-names" is put as an argument by the user, otherwise it is False
def handleArguments():

#   Makes a False name boolean that only becomes True if a spacific condition is met
    nameCheck = False

#   Tests if only one argument is there (program name)
    if len(sys.argv) == 1:
        stars_location_file = input('Enter a stars location file: ')
        if os.path.isfile(stars_location_file) == False:                # Checks if the file is valid and exists
            print('Error: Could not find a stars_location_file!')
            sys.exit(1)                                                 # Exits the system if condition is not met

#   Tests for 2 arguments (program name and "-names")
    elif len(sys.argv) == 2 and sys.argv[1] == "-names":
        stars_location_file = input('Enter a stars location file: ')    # Prompts user to give a star file if it isn't an argument
        
#       If "-names" is an argument, makes a True boolean for writing star names down
        nameCheck = True

        if os.path.isfile(stars_location_file) == False:
            print('Error: Could not find a stars_location_file!')
            sys.exit(1)

#   Tests for 2 arguments (program name and stars_location_file)
    elif len(sys.argv) == 2 and sys.argv[1] != "-names":
        stars_location_file = sys.argv[1]
        if os.path.isfile(stars_location_file) == False:
            print('Error: Could not find a stars_location_file!')
            sys.exit(1)

#   Tests for 3 arguments (program name, stars_location_file as second arg, and "-names" as third arg)
    elif len(sys.argv) == 3 and (sys.argv[1] != "-names" and sys.argv[2] == "-names"):
        stars_location_file = sys.argv[1]
        nameCheck = True
        if os.path.isfile(stars_location_file) == False:
            print('Error: Could not find a stars_location_file!')
            sys.exit(1)

#   Tests for 3 arguments (program name, "-names" as second arg, and stars_location_file" as third arg)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-names" and sys.argv[2] != "-names"):
        stars_location_file = sys.argv[2]
        nameCheck = True
        if os.path.isfile(stars_location_file) == False:
            print('Error: Could not find a stars_location_file!')
            sys.exit(1)

#   Tests for 3 arguments (program name and "-names" is neither of the other 2 arguments)
    elif len(sys.argv) == 3 and (sys.argv[1] != "-names" and sys.argv[2] != "-names"):
        print('Error: Invalid arguments, one argument must be "-names" and one must be a stars_location_file!')
        sys.exit(1)

#   Tests for 3 arguments (program name and "-names" is both of the other 2 arguments)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-names" and sys.argv[2] == "-names"):
        print('Error: Invalid arguments, one argument must be a stars_location_file!')
        sys.exit(1)

#   Condition for anything other than the previous conditions
    else:
        print('Error: Too many arguments')
        sys.exit(1)

    return stars_location_file, nameCheck

# Opens the stars_location_file and makes sure the file is the right file type (csv file)
# Reads every line of the file if it opens, splits the ",", and splits the ";" from the last index (name of star)
# Strips '\n' from the last index
# Appends the first, second, and fifth value in each split line into a list
# Appends all the named stars into a dictionary with the names as the key and each value
# Parameters:
#   stars_location_file: the star file that the user puts into the program
# Usage: readStarInformation(stars_location_file)
# Returns:
#   starList: the list of the (x, y, mag) tuples of each line in the star_location_file
#   starDict: A dictionary of the named stars with the name of the star as the key and the (x, y, mag) tuples as the values
def readStarInformation(stars_location_file):

    starList = []                                   # Empty list for all the stars
    starDict = {}                                   # Empty dictionary for the named stars

#   Try/except for stars_location_file so that only a valid csv file will open
    try:
        starsFile = open(stars_location_file, 'r')  # Opens stars_location_file which user inputted or made as an argument
    except:
        print('Error: Invalid file type!')
        sys.exit(1)
    try:
        starsFileLines = starsFile.readlines()          # Reads all lines of starsFile
    except:
        print('Error, information not of right type!')
        sys.exit(1)
    for line in starsFileLines:                     # for loop for every line in starFileLines
        starLine = line.split(',')                  # splits each line for the ','
#       Condition where it makes sure that the list made from the split is of length 7, otherwise it is an invalid file
        if len(starLine) == 7:
            try:
                starNameStrip = starLine[6].rstrip('\n')    # Strips the last value in the list of '\n', leaving a blank string
                starName = starNameStrip.split(';')         # Splits ';' from the last value in the list if there are 2 names for a star
                starNameTuple = tuple(starName)             # Makes the list into a tuple

#               Joins the starName list into a single string for the print statement later on
#               Code recieved from: https://www.tutorialspoint.com/python3/string_join.htm
                nameJoined = ', '.join(starName)

                x = float(starLine[0])                      # X-axis variable for the star                      
                y = float(starLine[1])                      # Y-axis variable for the star   
                mag = float(starLine[4])                    # Magnitude for the star
                starTuple = (x, y, mag)                     # Makes a tuple for the x, y, and mag values of the star
                starList.append(starTuple)                  # Append the starTuple to starList

#               Condition for if the starNames are not a blank string from the stripping of '\n' earlier
                if starNameTuple[0] !='':
                    for i in starNameTuple:
                        starDict[i] = starTuple             # Appends the star tuple into starDict with the star name as the key
                    print (f'{nameJoined} is at {(x, y)} with magnitude {mag}')
            except:
                print('Error, information not of right type!')
                sys.exit(1)
        else:
            print('Error: length of list in the line of the file is not 7!')
            sys.exit(1)
    try:
        starsFile.close()
    except:
        print('Error: could not close file!')
        sys.exit(1)
    return starList, starDict

# Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
# Parameters:
#   XO, YO: the pixel location of the origin of the graph, they will be 300 (constant)
#   RATIO: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels), it equals 300 (constant)
#   x, y: the graph location to change into a screen (pixel-based) location
# Usage: screenCoor(XO, YO, RATIO, x, y)
# Returns: 
#   (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
def screenCoor(XO, YO, RATIO, x, y):
    (screenX, screenY) = (((XO + (RATIO * x)), (YO + (RATIO * y)))) # Formula from the assignment 2 PDF, page #2
    return (screenX, screenY)

# Draw in the window an x-axis and y-axis as well as ticks at increments of 0.25 (constant) for the x and y
# Usage: drawXAxisAndYAxis(pointer, XO, YO, RATIO)
# Parameters:
#   pointer: the turtle drawing object
#   XO, YO : the pixel location of the origin of the  graph
#   RATIO: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels), will be 300 (constant)
# Returns: Nothing
def drawXAxisAndYAxis(pointer, XO, YO, RATIO):
    x = -1                                                      # Sets x as a local variable for the function
    y = 0                                                       # Sets y as a local variable for the function
    text = -1.0                                                 # Sets text as a local variable for the a written value of x and y

    (screenX, screenY) = screenCoor(XO, YO, RATIO, x, y)
    pointer.up()                                                # Takes pointer pen off screen
    pointer.goto(screenX, screenY)                              # Goes to where x = -1 and y = 0

    while screenX < WIDTH:                                      # Pointer draws until it reaches the end of the turtle screen on x-axis
        pointer.down()                                          # Puts pointer pen on screen
        (screenX, screenY) = screenCoor(XO, YO, RATIO, x, y)    # Calls the screenCoor() function
        pointer.goto(screenX, screenY)                          # pointer moves to (screenX, screenY)
        pointer.goto(screenX, screenY + LABELTICK)
        if x != 0:                                              # Writes under the x-axis as long it isn't 0
            pointer.write(text, False, align = "center")
        pointer.goto(screenX, screenY - LABELTICK)              
        pointer.up()
        pointer.goto(screenX, screenY)
        x += INCREMENT                                          # Increments x by the constant INCREMENT
        text += INCREMENT                                       # Increments text by the constant INCREMENT

    x = 0                                                       # Resets x to 0
    y = -1                                                      # Makes y -1
    text = -1.0                                                 # Resets text to -1.0

    (screenX, screenY) = screenCoor(XO, YO, RATIO, x, y)
    pointer.up()
    pointer.goto(screenX, screenY)

    while screenY < HEIGHT:                                     # Pointer draws until it reaches the end of the turtle screen on y-axis
        pointer.down()
        (screenX, screenY) = screenCoor(XO, YO, RATIO, x, y)
        pointer.goto(screenX, screenY)
        pointer.goto(screenX + LABELTICK, screenY)
        if y != 0:                                              # Writes beside the y-axis as long it isn't 0
            pointer.write(text, False)
        pointer.goto(screenX - LABELTICK, screenY)              
        pointer.up()
        pointer.goto(screenX, screenY)
        y += INCREMENT                                          # Increments y by the constant INCREMENT
        text += INCREMENT                                       
    pass

# Takes each tuple in the starList and gets and x, y, and magnitude
# Draws the stars in gray as a circle using its x and y coordinates and using mag for the radius which is how big the star gets drawn
# Takes each key in starDict and uses the key to find the x, y, and mag to draw named stars in white
# Parameters:
#   pointer: turtle pen that draws
#   starList: List of stars x, y, and mag variables returned from readStarInformation()
#   starDict: Dictionary of named stars taken from readStarInformation()
#   nameCheck: boolean taken from handleArguments() that is True if -"names" is a command line argument
# Usage: drawStars(pointer, starList, starDict, nameCheck)
# Returns: Nothing
def drawStars(pointer, starList, starDict, nameCheck):
    for i in starList:
        pointer.pencolor(STARCOLOR2)
        pointer.fillcolor(STARCOLOR2)
        radius = (10 / (i[2] + 2) / 2)                  # Formula from assignment #3 PDF page #6
        x = i[0]                                        # x is the first value of the tuple in the list
        y = i[1]                                        # y is the second value of the tuple in the list
        pointer.up()
        pointer.goto(screenCoor(XO, YO, RATIO, x, y))
        pointer.down()
        pointer.begin_fill()                            # Fills circle
        pointer.circle(radius)                          # Draws circle
        pointer.end_fill()
    for name in starDict:
        pointer.pencolor(STARCOLOR)
        pointer.fillcolor(STARCOLOR)
        radius = (10 / (starDict[name][2] + 2) / 2)
        x = starDict[name][0]                           # x is the first value from the tuple for a corresponding name key
        y = starDict[name][1]                           # y is the second value from the tuple for a corresponding name key
        pointer.up()
        pointer.goto(screenCoor(XO, YO, RATIO, x, y))
        pointer.down()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
        if nameCheck == True:                           # Checks if the nameCheck from handleArguments() is True for writing star names
            pointer.write(name,font=("Arial", 5, "normal"))
    pass

# Opens the constellationFile and makes sure the file is the right file type (csv file)
# Reads every line of the file if it opens, splits the "," from the 2 names
# Strips '\n' from the last index
# Takes the first line of the constellation File and pops it to get the name of the constellation
# Appends the constellation names into a list for use in the drawConstellations() function
# Parameters:
#   constellationFile: Prompted constellation file in main function 
#   starDict: dictionary of stars returned from readStarInformation() function
# Usage: readConstellations(constellationFile, starDict)
# Returns:
#   constellationList: A list of star names in a constellation from the given file from the user
#   constellationName: The name of the constellation of the file given
def readConstellations(constellationFile, starDict):
    try:                                                # Try/except to open constelationFile to make sure its a csv file
        constellation = open(constellationFile, 'r')    # Opens constellationFile
    except:
        print('Invalid file type!')
        sys.exit(1)
    try:
        constellationLines = constellation.readlines()  # Reads every line of constellation
    except:
        print('Error, information not of right type!')
        sys.exit(1)

    constellationList = []                              # Empty list for constellation names in the file

    for i in constellationLines:
        try:
            stars = i.strip('\n').split(',')            # strips '\n' and splits ',' for each line in the file
        except:
            print('Invalid information type in file!')
            sys.exit(1)
        if len(stars) == 1:                             # Condition for the first line which is the constellation name
            constellationName = stars.pop()             # Takes out constellation's name from the list

#       Conditions for the other lines which are all length 2 and if they are in the starDict or not
        elif len(stars) == 2 and stars[0] in starDict and stars[1] in starDict:
            constellationList.append(stars)             # Appends the stars names in the constellation file into a list 
        elif len(stars) == 2 and (stars[0] not in starDict or stars[1] not in starDict): 
            print('Invalid values in file, one or both values are not named stars from the star file!')
            sys.exit(1)        

        else:                                           # Condition to weed out any file that doesn't have lines with length 1 or 2
            print('Error: length of a line of list of stars must be 1 or 2!')
            sys.exit(1)

    namesInConstellation = []                           # Empty list to be used for the print function of constellations

#   Appends each star name that is part of the constellation form the file into a list to print later on (if the list isn't empty)
    if constellationList != []:
        for c in constellationList:
            if (c[0] not in namesInConstellation):      # Makes sure that names are not repeated in list
                namesInConstellation.append(c[0])
            if (c[1] not in namesInConstellation):
                namesInConstellation.append(c[1])
    else:
        print('Error: constellation list is empty, constellation file has no starting star names and finishing star names!')
        sys.exit(1)
    constellationSet = ', '.join(namesInConstellation)  # Joins the names in list into a string
    try:                                                # Makes sure there is a constellation name from the file
#       Prints a statement of the stars which are in the constellation based on the constellation file
        print(f'{constellationName} constellation contains {constellationSet}')
    except:
        print('Error: No constellation name!')
        sys.exit(1)

    try:                                                # Makes sure it closes file properly
        constellation.close()
    except:
        print('Error: Could not close file!')
        sys.exit(1)

    return constellationList, constellationName

# Takes the first index and second index of the constellationList
# Looks in the starDict for if those indices are the same as any key in starDict
# If that condition is true, the pointer will draw from the first index of constellationList to the second index
# When drawing, the first index of the key in the dictionary is x and the second index is y
# It also makes a list for the x values of the stars in the constellation and y values to be used for the constellationBox() function
# Parameters:
#   starDict: dictionary of all named stars
#   constellationList: List of all stars in the constellation that the user inputs
#   pointer: Turtle drawing pen
# Usage: drawConstellations(starDict, constellationList, pointer)
# Returns:
#   constellationBoxX: A list of all the x values which were of the stars in the constellation
#   constellationBoxY: A list of all the y values which were of the stars in the constellation
def drawConstellations(starDict, constellationList, pointer):
    constellationBoxX = []                                      # Empty list of x values of stars
    constellationBoxY = []                                      # Empty list of y values of stars
    for edge in constellationList:
        start = edge[0]                                         # The first name in the constellationList
        finish = edge[1]                                        # The second name in the constellationList
        pointer.up()
        if start in starDict:                                   # If the first name is in the starDict, pointer goes to start
            x = starDict[start][0]
            y = starDict[start][1]
            constellationBoxX.append(x)
            constellationBoxY.append(y)
            pointer.goto(screenCoor(XO, YO, RATIO, x, y))
            pointer.down()
        if finish in starDict:                                  # If the second name is in starDict, pointer draws from start to finish
            x = starDict[finish][0]
            y = starDict[finish][1]
            constellationBoxX.append(x)
            constellationBoxY.append(y)
            pointer.goto(screenCoor(XO, YO, RATIO, x, y))
            pointer.up()

    return constellationBoxX, constellationBoxY

# Sorts the constelattionBox list from smallest to biggest
# Takes the xmin, xmax, ymin, and ymax from the lists and makes a bound box around them with a little extra space (PADDING constant)
# Writes the constellation above the box it correlates to
# Parameters:
#   constellationBoxX: A list of all the x values which were of the stars in the constellation
#   constellationBoxY: A list of all the y values which were of the stars in the constellation
#   pointer: Turtle drawing pen
#   constellationName: The name of the constellation of the file given
# Usage: constellationBox(constellationBoxX, constellationBoxY, pointer, constellationName)
# Returns: Nothing
def constellationBox(constellationBoxX, constellationBoxY, pointer, constellationName):

    constellationBoxX.sort()                # Sorts list
    constellationBoxY.sort()                # Sorts list

#   Finds lowest and highest x and y values to make bounding box around constellation
    xmin = constellationBoxX[0]
    xmax = constellationBoxX[-1]
    ymin = constellationBoxY[0]
    ymax = constellationBoxY[-1]

#   x value in middle of bounding box
    halfX = (xmax + xmin) / 2

    pointer.color(PADDINGCOLOR)
    pointer.up()

#   Same formula as used in screenCoor() function except xmax, xmin, ymin, and ymax values are used instead of x and y
#   PADDING constant used to move a little bit above the x and y values to allow stars in constellation to be seen in bounding box
    pointer.goto(xmax * RATIO + XO + PADDING, ymax * RATIO + YO + PADDING)
    pointer.down()
    pointer.goto(xmax * RATIO + XO + PADDING, ymin * RATIO + YO - PADDING)
    pointer.goto(xmin * RATIO + XO - PADDING, ymin * RATIO + YO - PADDING)
    pointer.goto(xmin * RATIO + XO - PADDING, ymax * RATIO + YO + PADDING)
    pointer.goto(xmax * RATIO + XO + PADDING, ymax * RATIO + YO + PADDING)
    pointer.up()

#   Moves pointer to middle of upper part of bounding box in order to write constelation name above box
    pointer.goto(halfX * RATIO + XO + PADDING, ymax * RATIO + YO + PADDING)
    pointer.down()
    pointer.write(constellationName, False, align='center')

#   Creates a .dat file for the bounding box of the constellation with x and y values
    f = open(f'{constellationName}_box.dat', 'w+')
    f.write(f'xmax: {xmax}\nxmin: {xmin}\nymax: {ymax}\nymin: {ymin}')
    f.close
    pass

# Returns a string of the colour to use for the current constellation being drawn
# This colour is chosen based on which how many expression have previously been drawn
# The counter starts at 0, the first or 0th expression, should be red, the second green, the third yellow
# Then loops back to red, then green, then yellow, again
# Parameters:
#   counter: an integer where the value is a count (starting at 0) of the expressions drawn
# Returns:
#   0 -> "red", 1 -> "green", 2 -> "yellow", 3 -> "red", 4 -> "green", etc.
def getColor(counter):
    if counter % 3 == 0:    #Draw a red line if the remainder of the value divided by 3 is 0
        return "red"
    if counter % 3 == 1:    #Draw a green line if the remainder of the value divided by 3 is 1
        return "green"
    else:                   #Draw a blue line otherwise
        return "yellow"

# Setup of turtle screen before we draw
# Usage: setup()
# Parameters: None
# Returns: pointer
def setup():
    pointer = turtle.Turtle()                           # pointer is the turtle pen
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)                   # Sets the turtle screen
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)                     # Sets background color to black
    pointer.up()

    return pointer

def main():
    try:
#       Handle arguments
        stars_location_file, nameCheck = handleArguments()
#       Read star information from file (function)
        starList, starDict = readStarInformation(stars_location_file)
#       Setup turtle
        pointer = setup()
#       Set axis color
        pointer.color(AXISCOLOR)
#       Draw Axes (function)
        drawXAxisAndYAxis(pointer, XO, YO, RATIO)
#       Draw Stars (function)
        drawStars(pointer, starList, starDict, nameCheck)
#       Loop getting filenames
        constellationFile = input('Please enter a constellation file: ')
        counter = 0
        while constellationFile != "":
#           While constellationFile does not exist, it keeps looping for an existing file
            while constellationFile != "" and os.path.isfile(constellationFile) == False:
                constellationFile = input('Invalid file, please enter another constellation file: ')
            while constellationFile == "":
                print('Error: entered a blank string')
                sys.exit(1)
#           Read constellation file (function)
            constellationList, constellationName = readConstellations(constellationFile, starDict)
#           Loops colors for constellation drawing
            pointer.color(getColor(counter))
#           Draw Constellation (function)
            constellationBoxX, constellationBoxY = drawConstellations(starDict, constellationList, pointer)
            counter += 1
            #Draw bounding box (Bonus) (function)
            constellationBox(constellationBoxX, constellationBoxY, pointer, constellationName)
            constellationFile = input('Please enter another constellation file: ')
        print('Error: entered a blank string')
        sys.exit(1)
    except SystemExit as error:                     # Exit statement for sys.exit(1)
        if int(error.code) == 1:
            print('Error 1: Program will exit!')
    pass

main()