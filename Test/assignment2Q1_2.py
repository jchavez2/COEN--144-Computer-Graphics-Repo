# Author: Jason Chavez
# File: assignment2Q1.py
# Description: This file 

# object representation

from PIL import Image, ImageDraw
import webbrowser
import math
import csv
import array as arr


filename = "assignement2Q1_2.png"
img = Image.new('RGB', (900, 900))

# this list hold all vertices
# you can use append() to add all x, y, z
# into it. the format could be like this:
# [[x1, y1, z1], [x2, y2, z2],......]
vertices = []

#Eye Coordinates intilization:
eyeCoordinates = [3.0,1.0,3.0]
#Normal vector Intialization:
Norm = [1.1,1.2,1.3]
#top constant of normal equation:
topConst = (Norm[0] * eyeCoordinates[0]) + (Norm[1] * eyeCoordinates[1]) +(Norm[2] * eyeCoordinates[2])



# Method 'project' It then divides by the point z to obtain a projected point on the 2D plane.

def project(faceVertList):
    pointList = []
    x = float(faceVertList[0])
    y = float(faceVertList[1])
    z = float(faceVertList[2])
    #Calculate the value for the t! 
    bottom = (Norm[0] * x) + (Norm[1] * y) + (Norm[2] *z)
    t = topConst / bottom
    #Calculate for the x and y:
    x = t * x
    pointList.append(x)
    y = t * y
    pointList.append(y)
    pointList.append(1.0)
    return pointList 

def Translate(points, transX, transY):
    newList = []
    newPointx = points[0] + transX
    newList.append(newPointx)
    newPointy = points[1] + transY
    newList.append(newPointy)
    newList.append(1.0)
    return  newList

def rotate(points, rotateAng):
    rads = (math.pi / 180) * rotateAng
    newList = []
    newPointx = (points[0] * math.cos(rads)) - (points[1] * math.sin(rads))
    newList.append(newPointx)
    newPointy = (points[0] * math.sin(rads)) + (points[1] * math.cos(rads))
    newList.append(newPointy)
    newList.append(1.0)
    return newList

def scale(points, scaleX, scaleY):
    newList = []
    newPointx = points[0] * scaleX
    newList.append(newPointx)
    newPointy = points[1] * scaleY
    newList.append(newPointy)
    newList.append(1)
    return newList

#read in face vertices
with open('face-vertices.data', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Transfer face-vertices to 'vertices' list using the 'append()' method
    for row in csv_reader:    
        vertices.append(row)

#Declare img and define draw pixel method:            
pixels = img.load()
def draw_pixel(x,y, color):
    pixels[x,y] = (color,color,0)



#read index
with open('face-index.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    #Draw points in the reading of the index:
    for index in csv_reader:
        if line_count < len(index):
            print( int(index[0]), int(index[1]), int(index[2]) )
        
        for i in range(0,3):  
            if line_count < len(index):
                j = int(index[i])
                newPoints = project(vertices[j])
            xc = 450
            yc = 450
            newPoints = Translate(newPoints, -xc, -yc)
            newPoints = rotate(newPoints, 180.0)
            newPoints = scale(newPoints, 2.350, 2.350)
            newPoints = Translate(newPoints, xc, yc)
            print("\n", newPoints, "\n")
            # if(xWMax < newPoints[0]):
            #     xWMax = newPoints[0]
            # if(xWMin > newPoints[0]):
            #     xWMin = newPoints[0]
            # if(yWMax < newPoints[1]):
            #     yWMax = newPoints[1]
            # if(yWMin > newPoints[1]):
            #     yWMin = newPoints[1]
            # if(zWMax > newPoints[2]):
            #     zWMax = newPoints[2]
            # if(zWMin < newPoints[2]):
            #     zWMin = newPoints[2]
            if(newPoints[0] <= 900 and newPoints[0] >= -900):
                if(newPoints[1] <= 900 and newPoints[1] >= -900):
                    draw_pixel(abs(int(newPoints[0])), abs(int(newPoints[1])), 205) 
    # print('xWmax= ', xWMax)
    # print('xWmin= ', xWMin)
    # print('yWMax= ', yWMax)
    # print('yWMin= ', yWMin)
    # print('zWmax= ', zWMax)
    # print('zWmin= ', zWMin)

#img.show()

img.save(filename)
webbrowser.open(filename)
