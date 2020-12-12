#Author: Jason Chavez
#File: assignment1P1.py
#Description: This file rasters a circle using Bresenham's algorithm. 
#The file is saved as an image and displayed using the computers perfered photo drawing software.  

from PIL import Image
import webbrowser       #Necessary for Windows to open in Paint
filename = "CircleRasterization.png"
img= Image.new('RGB', (320, 240))
pixels= img.load()

#Intialize Varibles:
R = 50
d = (5/4) - R
x = 0 
y = R
xc = 160
yc = 120

#Function to call to draw circle:
def drawCircle(xc,yc,x,y):
    #Rasterize 8-Coordinates and alternate signs 
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
    l = 0

#Reference Points
pixels[0,0] = (12,110,0)
pixels[0,1] = (255,233,2)
pixels[160,120] = (0,100,100)

#Algorithum
drawCircle(xc,yc,x,y)
while y >= x:
    if d < 0:
        d += 2 * x + 3
        x+=1
    else:
        d += 2 * (x  - y) + 5
        x+=1
        y-=1
    drawCircle(xc,yc,x,y)
#Commented out the show function since it does no work for windows systems
#img.show()

#Using the save() function as a subsustuite to display image along with the webbrowser.open() function.
img.save(filename)
webbrowser.open(filename)

