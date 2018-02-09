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
def runCircle(radius):
    prepareGUI()
    start = True
    while start == True:
        circle(radius)
        rotation(rot)
        
###-------------------------------------------###

def rectangle(dist):
    dist2 = int(dist * 0.5)
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist2)
    turtle.right(90)
    turtle.forward(dist)
    turtle.right(90)
    turtle.forward(dist2)
#Call prepareGUI and run rectangle loop
def runRectangle(dist, rot):
    prepareGUI()
    start = True
    while start == True:
        rectangle(dist)
        rotation(rot)

###-------------------------------------------###
        
#Basic function for torus
def torus(radius):
    turtle.circle(radius)
#Call prepareGUI and run loop for torus
def runTorus(radius,rot,dist):
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
    prepareGUI()
    start = True
    while start == True:
        triangle(side)
        rotation(rot)
        

###--------------------------------------------###



#Basic spiral
def runSpiral(dist):
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(1)
        dist = dist + 0.0005

#square spiral
def runSqSpiral(dist):
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(91)
        dist = dist + 1
        
#hexagonal spiral
def runHexSpiral(dist):
    prepareGUI()
    start = True
    while start == True:
        turtle.forward(dist)
        turtle.right(61)
        dist += 1
        
###--------------------------------------------###

        
#Prep GUI, set turtle speed and visibility, set background and line color
def prepareGUI():
    turtle.speed(0)
    turtle.ht()
    turtle.bgcolor("black")
    turtle.color("white")

#Main method
def main():

    choice = 0
    while choice != QUIT_CHOICE:
        display_menu()

        choice = int(input("Enter your choice:"))
        if choice == RECTANGLE:
            side = int(input("Input a side length"))
            rot = int(input("Input a value for rotation:"))
            runRectangle(side, rot)
        elif choice == CIRCLE:
            radius = int(input("Input a value for radius:"))
            runCircle(radius)
        elif choice == TORUS:
            radius = int(input("Input a value for radius:"))
            rot = int(input("Input a value for rotation:"))
            dist = int(input("Input a value for center radius:"))
            runTorus(radius, rot, dist)
        elif choice == TRIANGLE:
            side = int(input("Input a value for side length:"))
            rot = int(input("Input a value for rotation:"))
            runTriangle(side, rot)
        elif choice == SPIRAL:           
            dist = int(input("Input a value for distance:"))
            runSpiral(dist)
        elif choice == SQUARE_SPIRAL:
            dist = int(input("Input a value for distance:"))
            runSqSpiral(dist)
        elif choice == HEX_SPIRAL:
            dist = int(input("Input a value for distance:"))
            runHexSpiral(dist)
        elif choice == QUIT_CHOICE:
            print("Exiting the program!")
        else:
            print("Invalid input!")
            
            
#Main program body

main()
    
