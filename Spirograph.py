import turtle


#Menu Choices
RECTANGLE = 1
CIRCLE = 2
TORUS = 3
TRIANGLE = 4
SPIRAL = 5
SQUARE_SPIRAL = 6
HEX_SPIRAL = 7
QUIT_CHOICE = 8

#Prepare menu
def display_menu():
    print("Welcome to the show! Select an option:")
    print("-------------------------------------")
    print("1)Rectangle")
    print("2)Circle")
    print("3)Torus")
    print("4)Triangle")
    print("5)Spiral")
    print("6)Square Spiral")
    print("7)Hex Spiral")
    print("8)Quit")

#Set right rotation 
def rotation(rot):
    turtle.right(rot)
   
###-------------------------------------------###

#Basic function for circle    
def circle(radius):
    turtle.circle(radius)

#Call prepareGUI and run circle loop   
def runCircle():
    CircString()
    radius = int(input("Input a value for radius: "))
    rot = int(input("Input a value for rotation: "))
    prepareGUI()
    start = True
    while start == True:
        circle(radius)
        rotation(rot)
    
    
###-------------------------------------------###

def rectangle(dist1, dist2):
    
    turtle.forward(dist1)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.right(90)
    turtle.forward(dist1)
    turtle.right(90)
    turtle.forward(dist2)
#Call prepareGUI and run rectangle loop
def runRectangle():
    RectString()
    side1 = int(input("Input the first side length: "))
    side2 = int(input("Input the second side length: "))
    rot = int(input("Input a value for rotation: "))
    prepareGUI()
    start = True
    while start == True:
        rectangle(side1, side2)
        rotation(rot)

###-------------------------------------------###
        
#Basic function for torus
def torus(radius):
    turtle.circle(radius)
#Call prepareGUI and run loop for torus
def runTorus(radius,rot,dist):
    TorString()
    radius = int(input("Input a value for radius: "))
    rot = int(input("Input a value for rotation: "))
    dist = int(input("Input a value for center radius: "))                
    prepareGUI()
    start = True
    while start == True:
        torus(radius)
        rotation(rot)
        turtle.forward(dist)
###-------------------------------------------###

        

#Basic function for triangles
def triangle(side):
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60)
    turtle.forward(side)
    turtle.right(60)
#Call prepareGUI and run loop for triangles    
def runTriangle(side, rot):
    TriString()
    side = int(input("Input a value for side length: "))
    rot = int(input("Input a value for rotation: "))
    prepareGUI()
    start = True
    while start == True:
        triangle(side)
        rotation(rot)
        

###--------------------------------------------###



#Basic spiral
def runSpiral():
    SpirString()
    dist = int(input("Input a value for distance: "))
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(1)
        dist = dist + 0.0005

#square spiral
def runSqSpiral():
    SquareSpirString()
    dist = int(input("Input a value for distance: "))
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(91)
        dist = dist + 1
        
#hexagonal spiral
def runHexSpiral():
    HexSpirString()
    dist = int(input("Input a value for distance: "))
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(61)
        dist += 1

###--------------------------------------------###

        
#Prep GUI, set turtle speed and visibility, set background and line color
def prepareGUI():

    wn = turtle.Screen()

    rootwindow = wn.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
        
    turtle.speed(0)
    turtle.ht()
    turtle.bgcolor("black")
    turtle.color("white")
    turtle.pensize()

    

###-------------------------------------------###

#ToString for all options.

def RectString():
    RString = """

    Rectangle: Spirograph based on rectangular shapes. 
    Recommended Inputs: 
        Side Length: 20-100
        Rotation: 1-179
        
    """
    print(RString)

def CircString():
    CString = """

    Circle: Spirograph based on circular shapes. 
    Recommended Inputs: 
        Radius: 5-100
        Rotation: 1-179
        
    """
    print(CString)

def TorString():
    TString = """

    Torus: Spirograph based on toroidal shapes.
    Recommended Inputs:
        Radius: 5-100
        Inner Radius: 5-100
        Rotation: 1-179

    """
    print(TString)

def TriString():
    TrString = """

    Triangle: Spirograph based on triangular shapes.
    Recommended Inputs:
        Side length: 5-100
        Rotation: 1-179
        
    """
    print(TrString)

def SpirString():
    SpString = """

    Spiral: Spiral design.  
    Recommended Inputs:
        Distance: 1-2
        
    """

def SquareSpirString():
    SqSpString = """

    Square Spiral: Ever expanding squares.
    Recommended Inputs:
        Side length: 5-100
        
    """
    print(SqSpString)

def HexSpirString():
    HexString = """

    Hexagonal Spiral: Ever expanding hexagons.
    Recommended Inputs:
        Side Length: 5-100

    """
    
#Main method
def main():

    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input("Enter your choice:"))
        if choice == RECTANGLE:
            runRectangle()
        elif choice == CIRCLE:
            runCircle()
        elif choice == TORUS:
            runTorus()
        elif choice == TRIANGLE:
            runTriangle()
        elif choice == SPIRAL:
            runSpiral()
        elif choice == SQUARE_SPIRAL:
            runSqSpiral() 
        elif choice == HEX_SPIRAL:
            runHexSpiral()
        elif choice == QUIT_CHOICE:
            print("Exiting the program! ")
        else:
            print("Invalid input! ")
            
            
#Main program body

main()
    
