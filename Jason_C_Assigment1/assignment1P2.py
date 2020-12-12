#Author: Jason Chavez
#File: assignment1P2.py
#Description: This file rasters a circle using Bresenham's algorithm.
#This is taken a step further by not only rastering the circle but also filling the circle 
#The file is saved as an image and displayed using the computers perfered photo drawing software. 

from PIL import Image
import webbrowser       #Necessary for Windows to open in Paint
filename = "CircleFill.png"
img= Image.new('RGB', (320, 240))
pixels= img.load()

#Intialize Varibles:
R = 50
d = (5/4) - R
x = 0 
y = R
xc = 160
yc = 120

#Function to fill circle
def circleFill(xc,yc,x,y):
    #Run loop to fill in pixels on y-axis
    i = yc - y
    while i < (yc + y):
        i += 1
        pixels[(xc + x), i] = (255,0,0)
        pixels[(xc - x), i] = (255,0,0)
    #Run loop to fill in pixels x-axis
    i = xc - y
    while i < (xc + y):
        i+=1
        pixels[i, (yc + x)] = (255,0,0)
        pixels[i, (yc - x)] = (255,0,0)

#Function to call to draw circle:
def drawEdgeCircle(xc,yc,x,y):
    #Intialize 8-Coordinates and alternate signs (with line fill)
    pixels[(xc + x),(yc + y)] = (255,0,0)
    pixels[(xc + y),(yc + x)] = (255,0,0) 
    x = -x
    pixels[(xc + x),(yc + y)] = (255,0,0)
    pixels[(xc + y),(yc + x)] = (255,0,0)
    y = -y
    pixels[(xc + x),(yc + y)] = (255,0,0)
    pixels[(xc + y),(yc + x)] = (255,0,0)
    x = -x
    pixels[(xc + x),(yc + y)] = (255,0,0)
    pixels[(xc + y),(yc + x)] = (255,0,0)

#Algorithum
circleFill(xc,yc,x,y)
drawEdgeCircle(xc,yc,x,y)
while y >= x:
    if d < 0:
        d += 2 * x + 3
        x+=1
    else:
        d += 2 * (x  - y) + 5
        x+=1
        y-=1
    circleFill(xc,yc,x,y)
    drawEdgeCircle(xc,yc,x,y)
    

#Commented out the show function since it does no work for windows systems
#img.show()

#Using the save() function as a subsustuite to display image along with the webbrowser.open() function.
img.save(filename)
webbrowser.open(filename)

