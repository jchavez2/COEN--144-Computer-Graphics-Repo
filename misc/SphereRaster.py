# This is a test file to rasterize a sphere within a scene

from PIL import Image, ImageDraw
import webbrowser
import math


filename = "SphereRaster.png"
img = Image.new('RGB', (1024, 1024))

pixels = img.load()

lightSrcCoordinates = [512, 512, 5]
eyeCoordiantes = [500, 100, 3]
R = 20
SphereCenter = [500, 700, 40]
SphereColor = [255, 20, 9]
backgroundColor = [255, 255, 255]


def RaySphereIntersection(Vec0, Vec1, SphCenCord, Rad):
    listOfValues = []
    changeValues = []
    quadCoeffs = []
    X0 = Vec0[0]
    Y0 = Vec0[1]
    Z0 = Vec0[2]
    X1 = Vec1[0]
    Y1 = Vec1[1]
    Z1 = Vec1[2]
    SphX = SphCenCord[0]
    SphY = SphCenCord[1]
    SphZ = SphCenCord[2]
    dx = X1 - X0
    changeValues.append(dx)
    dy = Y1 - Y0
    changeValues.append(dy)
    dz = Z1 - Z0
    changeValues.append(dz)
    a = (dx * dx) + (dy *dy) + (dz * dz)
    quadCoeffs.append(a)
    b = 2 * dx * (X0 - SphX) + 2 * dy * (Y0 - SphY) + 2 * dz * (Z0 - SphZ)
    quadCoeffs.append(b)
    c = (SphX * SphX) + (SphY * SphY) + (SphZ * SphZ) + (X0 *X0) +(Y0 * Y0) + (Z0 * Z0)  + (-2) * (SphX * X0 + SphY * Y0 + SphZ * Z0) -(Rad * Rad)
    quadCoeffs.append(c)
    dis = (b*b) - (4 * a * c)
    listOfValues.append(dis)
    listOfValues.append(changeValues)
    listOfValues.append(quadCoeffs)
    return listOfValues


for x in range(0, 1024):
    for y in range(0, 1024):
        temp = []
        temp.append(x)
        temp.append(y)
        temp.append(0)
        doubleListValues = RaySphereIntersection(eyeCoordiantes, temp, SphereCenter, R)
        if doubleListValues[0] < 0:
            doubleListValues2 = RaySphereIntersection(temp, lightSrcCoordinates, SphereCenter, R)
            if doubleListValues2[0] >= 0:
                pixels[x,y] = (127, 127, 127)
            else:
                pixels[x,y] = (backgroundColor[0], backgroundColor[1], backgroundColor[2])
        else:
            t = (-doubleListValues[2][1] - (math.sqrt(doubleListValues[0]))) / (2 * doubleListValues[2][0])
            pixels[x,y] = (250, 2, 120)
            


        
img.save(filename)
webbrowser.open(filename)
