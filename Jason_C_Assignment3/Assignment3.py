# Author: Jason Chavez
# File Name: Assignment3.py
# Description: This file produces a 2D image of at least 2 spheres that
# are projected onto the screen. 

from PIL import Image, ImageDraw
import webbrowser
import math

filename = "Assignment3.png"
img = Image.new('RGB', (1024, 1024))


# Defining x, y, & z coordinates for the Light Src and Eye. 
lightSrcCoordinates = [500.0, 500.0, -50.0]
eyeCoordiantes = [500.0, 10.0, 20.0]

# Defining the Sphere Properties:
R = 43
SphereCenter = [400.0, -100.0, 70.0]
SphereColor = [200, 0, 100]
R2 = 50
SphereCenter2 = [470.0, -10.0, 70.0]
SphereColor2 = [10, 20, 234]
#Other variables:
backgroundColor = [255, 255, 255]
Kdiff = 0.75
Kamb = 0.3
Kspec = 0.2112
temp = []
Vp = []

# Defining a basic drawing pixel function.
pixels = img.load()
def draw_pixel(x,y, Red, Yellow, Green):
    pixels[x,y] = (Red, Yellow, Green)


# Ambient Lighting Effect Function to get the light from the enviroment.
def ambLight(colorIntensity, surfaceCoeff):
    return int(colorIntensity * surfaceCoeff)


# Diffuse Reflection Lighting Effect: The amonunt of light that will be diffused within the object causing it to have a rougher appearance
def diffuseReflection(colorIntensity, surfaceCoeff, lightVec, NormalVec):
    Idiff = (colorIntensity * surfaceCoeff)
    cos = (surfaceCoeff * lightVec[0]) + (surfaceCoeff * lightVec[1]) + (surfaceCoeff * lightVec[2])
    #Light Vector Magnitude Componet 
    lightVectMag = (lightVec[0] * lightVec[0] ) + (lightVec[1] * lightVec[1]) + (lightVec[2] * lightVec[2])
    #Normal Vector Magitude Componet
    NormalVecMag = (NormalVec[0] * NormalVec[0]) + (NormalVec[1] * NormalVec[1]) + (NormalVec[2] * NormalVec[2])
    _cos = math.sqrt(lightVectMag) * math.sqrt(NormalVecMag)
    TotalCos = cos / _cos
    return int(Idiff * TotalCos)

#Specular Lighting Effect:  The amount of light that will be reflected off the surface of the object. 
def specularReflection(colorIntensity, surfaceCoeff, eyeVec, lightVec, normalVec, shinnyVar):
    Ispec = colorIntensity * surfaceCoeff
    halfVec = []
    eyeLightVec = []
    eyePlusLightVec = 0.0
    VecMag = 0
    cos = 0
    for i in range(0,2):
        newVecVal = eyeVec[i] + lightVec[i]
        eyeLightVec.append(newVecVal)
        eyePlusLightVec += (eyeLightVec[i] * eyeLightVec[i])
    eyePlusLightVec = math.sqrt(eyePlusLightVec) 
    for i in range(0,2):
        newVecVal = eyeLightVec[i] / eyePlusLightVec
        halfVec.append(newVecVal)
        cos += (halfVec[i] * normalVec[i])
        VecMag += (halfVec[i] * normalVec[i]) * (halfVec[i] * normalVec[i])
    _cos = math.sqrt(VecMag)
    TotalCos = cos / _cos
    TotalCos = TotalCos ** shinnyVar
    return int(Ispec * TotalCos)
     

# Lighting Intensity Function to process the lighting for each surface pixel in the scene.
def lightIntestity(lightVec, surfaceNorm, eyeVec):
    return 1

#To calcuate the normal vector when finding a pt on the sphere. 
def NormVector(Vecf, Veci, Radius):
    Norm = []
    Nx = ((Vecf[0] - Veci[0]) / Radius)
    Ny = ((Vecf[1] - Veci[1]) / Radius)
    Nz = ((Vecf[2] - Veci[2]) / Radius) 
    Norm.append(Nx)
    Norm.append(Ny)
    Norm.append(Nz)
    return Norm

# To Calculate the unit vector form the pt on the sphere to the light:
def LightVec(LightPts, SphPts):
    LV = []
    Lx = LightPts[0] - SphPts[0]
    Ly = LightPts[1] - SphPts[1]
    Lz = LightPts[2] - SphPts[2]
    Lmag = math.sqrt((Lx *Lx) + (Ly * Ly) + (Lz * Lz)) 
    Lx = Lx / Lmag
    LV.append(Lx)
    Ly = Ly / Lmag
    LV.append(Ly)
    Lz = Lz / Lmag
    LV.append(Lz)
    return LV

# Function to calculate the Intesection of a ray with two points, the 
# return variable listOfValues returns three things: the discrinmate, 
# the t value and the sphere corrdinates in a list.
def RaySphereIntersection(Vec0, Vec1, SphCenCord, Radius):
    listOfValues = []
    SphereCoords = []
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
    dy = Y1 - Y0
    dz = Z1 - Z0

    a = (dx * dx) + (dy * dy) + (dz * dz)
    b = 2 * dx * (X0 - SphX) + 2 * dy * (Y0 - SphY) + 2 * dz * (Z0 - SphZ)
    c = (SphX * SphX) + (SphY * SphY) + (SphZ * SphZ) + (X0 * X0) + (Y0 * Y0) + (Z0 * Z0)  - 2 * (SphX * X0 + SphY * Y0 + SphZ * Z0) - (Radius * Radius)
    dis = (b*b) - (4 * a * c)
    if dis >= 0:
        t = (-b - (math.sqrt(dis))) / (2 * a)
        newX = X0 + t * dx
        SphereCoords.append(newX)
        newY = Y0 + t * dy
        SphereCoords.append(newY)
        newZ = Z0 + t * dz
        SphereCoords.append(newZ)
        listOfValues.append(dis)
        listOfValues.append(t)
        listOfValues.append(SphereCoords)
    else:
        listOfValues.append(dis)
        listOfValues.append(0)
        listOfValues.append(0)
    return listOfValues

#   Double for loop to cylce through each pixel to calculate points on 
#   spheres and the pixels to draw! 
for x in range (0, 1024):
    for y in range (0, 1024):
        temp.append(x)
        temp.append(y)
        temp.append(0)
        # Sphere1/2 Values are lists that recieve three values: The discriminate, the t value and the three points on sphere to calculate for other vectors:
        Sphere1Values = RaySphereIntersection(eyeCoordiantes, temp, SphereCenter, R)
        Sphere2Values = RaySphereIntersection(eyeCoordiantes, temp, SphereCenter2, R2)
        #Conditions to check for drawing background, showadow or sphere colors.
        if Sphere1Values[0] < 0 or Sphere2Values[0] < 0:
            Sphere1Values2 = RaySphereIntersection(temp, lightSrcCoordinates, SphereCenter, R)
            Sphere2Values2 = RaySphereIntersection(temp, lightSrcCoordinates, SphereCenter2, R2) 
            if Sphere1Values2[0] >= 0 or Sphere2Values2[0] >= 0:
                pixels[x,y] = (127, 127, 127)
            else:
                pixels[x,y] = (backgroundColor[0], backgroundColor[1], backgroundColor[2])
        else:
            Sph1PtLight = RaySphereIntersection(Sphere1Values[2], lightSrcCoordinates, SphereCenter2, R2)
            Sph2PtLight = RaySphereIntersection(Sphere2Values[2], lightSrcCoordinates, SphereCenter, R)
            if Sph1PtLight[0] >= 0 or Sph2PtLight[0] >= 0 and Sphere1Values[2][2] >= Sphere2Values[2][2]: 
                colorambX = ambLight(SphereColor[0], Kamb)
                colorambY = ambLight(SphereColor[1], Kamb)
                colorambZ = ambLight(SphereColor[2], Kamb)
                pixels[x,y] = (colorambX, colorambY, colorambZ)
            elif Sph1PtLight[0] >= 0 or Sph2PtLight[0] >= 0 and Sphere1Values[2][2] < Sphere2Values[2][2]:
                colorambX = ambLight(SphereColor2[0], Kamb)
                colorambY = ambLight(SphereColor2[1], Kamb)
                colorambZ = ambLight(SphereColor2[2], Kamb)
                pixels[x,y] = (colorambX, colorambY, colorambZ)
            else:
                if Sphere1Values[0] >= 0:
                    Norm1 = NormVector(Sphere1Values[2], SphereCenter, R)
                    LV1 = LightVec(lightSrcCoordinates, Sphere1Values[2])
                    colorambX = ambLight(SphereColor[0], Kamb)
                    colorambY = ambLight(SphereColor[1], Kamb)
                    colorambZ = ambLight(SphereColor[2], Kamb)
                    colordiffX = abs(diffuseReflection(SphereColor[0], Kdiff, LV1, Norm1))
                    colordiffY = abs(diffuseReflection(SphereColor[1], Kdiff, LV1, Norm1))
                    colordiffZ = abs(diffuseReflection(SphereColor[2], Kdiff, LV1, Norm1))
                    colorTotalX = colorambX + colordiffX
                    colorTotalY = colorambY + colordiffY
                    colorTotalZ = colorambZ + colordiffZ
                    pixels[x,y] = (colorTotalX, colorTotalY, colorTotalZ)
                    Norm1.clear()
                    LV1.clear()
                else:
                    Norm2 = NormVector(Sphere2Values[2], SphereCenter2, R2)
                    LV2 = LightVec(lightSrcCoordinates, Sphere2Values[2])
                    colorambX = ambLight(SphereColor2[0], Kamb)
                    colorambY = ambLight(SphereColor2[1], Kamb)
                    colorambZ = ambLight(SphereColor2[2], Kamb)
                    colordiffX = abs(diffuseReflection(SphereColor2[0], Kdiff, LV2, Norm2))
                    colordiffY = abs(diffuseReflection(SphereColor2[1], Kdiff, LV2, Norm2))
                    colordiffZ = abs(diffuseReflection(SphereColor2[2], Kdiff, LV2, Norm2))
                    colorTotalX = colorambX + colordiffX
                    colorTotalY = colorambY + colordiffY
                    colorTotalZ = colorambZ + colordiffZ
                    pixels[x,y] = (colorTotalX, colorTotalY, colorTotalZ)
                    Norm2.clear()
                    LV2.clear()
        temp.clear()

#Commented out the show function since it does no work for windows systems
#img.show()

#Using the save() function as a subsustuite to display image along with the webbrowser.open() function.
img.save(filename)
webbrowser.open(filename)