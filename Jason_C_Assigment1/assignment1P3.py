#Author: Jason Chavez
#File: assignment1P3.py
#Description: This file rasters a circle using Bresenham's algorithm.
#This is taken a step further by not only rastering the circle but also filling the circle.
#Anti-alias is added to create a smothness effect. 
#The file is saved as an image and displayed using the computers perfered photo drawing software. 

from PIL import Image
import webbrowser       #Necessary for Windows to open in Paint
import math             #Necessary to calcuate perError in antiAlias function
filename = "CircleFill&Anti-Alias.png"
img= Image.new('RGB', (320, 240))
pixels= img.load()

#Intialize Varibles:
R = 50
d = (5/4) - R
x = 0 
y = R
xc = 160
yc = 120

#Function for Anti-Alias
def antiAlias(x,y):
    xcord = x * x
    ycord = y * y
    #calculate the percent error away from circle
    perError = R - math.sqrt(xcord + ycord) 
    perError = abs(perError)
    if perError < .1:
        return 255
    elif perError < .2:
        return 230
    elif perError < .3:
        return 204
    elif perError < .4:
        return 179
    elif perError < .5:
        return 153
    elif perError < .6:
        return 128
    elif perError < .7:
        return 102
    elif perError < .8:
        return 77
    elif perError < .9:
        return 51
    else:
        return 26



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
    #The antiAlias function is called witin this function to calcuate the amount of intensity for the color
    shade = antiAlias(x, y)
    pixels[(xc + x),(yc + y)] = (shade,0,0)
    pixels[(xc + y),(yc + x)] = (shade,0,0) 
    x = -x
    pixels[(xc + x),(yc + y)] = (shade,0,0)
    pixels[(xc + y),(yc + x)] = (shade,0,0) 
    y = -y
    pixels[(xc + x),(yc + y)] = (shade,0,0)
    pixels[(xc + y),(yc + x)] = (shade,0,0) 
    x = -x
    pixels[(xc + x),(yc + y)] = (shade,0,0)
    pixels[(xc + y),(yc + x)] = (shade,0,0) 

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

