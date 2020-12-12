# Author: Jason Chavez
# File Name: rayCasting.py
# Description: This file produces a 2D image of at least 2 spheres that
# are projected onto the screen. 

from PIL import Image, ImageDraw
import webbrowser
import math

filename = "rayCasting.png"
img = Image.new('RGB', (1024, 1024))


# Defining x, y, & z coordinates for the Light Src and Eye. 
lightSrcCoordinates = [512.0, 512.0, 5.0]
eyeCoordiantes = [500.0, 270.0, 2.0]

# Defining the Sphere Properties:
R = 40
SphereCenter = [500.0, 70.0, 45.0]
SphereColor = [255, 20, 9]
backgroundColor = [255, 255, 255]
Norm = []
LV = []

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
    for i in range(0,2):
        newVecVal = eyeVec[i] + lightVec[i]
        eyeLightVec.append(newVecVal)
        eyePlusLightVec += (eyeLightVec[i] * eyeLightVec[i])
    eyePlusLightVec = math.sqrt(eyePlusLightVec) 
    for i in range(0,2):
        newVecVal = eyeLightVec[i] / eyePlusLightVec
        halfVec.append(newVecVal)
        cos += (halfVec[i] * normalVec[i])
        halfVecMag += (halfVec[i] * halfVec[i])
        normalVecMag += (normalVec[i] * normalVec[i])
    _cos = math.sqrt(halfVec) * math.sqrt(normalVec)
    TotalCos = cos / _cos
    TotalCos = TotalCos ** shinnyVar
    return int(Ispec * TotalCos)
     

# Lighting Intensity Function to process the lighting for each surface pixel in the scene.
def lightIntestity(lightVec, surfaceNorm, eyeVec):
    return 1

z = 0
#   Double for loop to cylce through each pixel to calculate points on 
#   spheres and the pixels to draw! 
for x in range (0, 1024):
    for y in range (0, 1024):
        dx = x - eyeCoordiantes[0]
        dy = y - eyeCoordiantes[1]
        dz = 0 - eyeCoordiantes[2]

        a = (dx * dx) + (dy *dy) + (dz * dz)
        b = 2 * dx * (eyeCoordiantes[0] - SphereCenter[0]) + 2 * dy * (eyeCoordiantes[1] - SphereCenter[1]) + 2 * dz * (eyeCoordiantes[2] - SphereCenter[2])
        c = (SphereCenter[0] * SphereCenter[0]) + (SphereCenter[1] * SphereCenter[1]) + (SphereCenter[2] * SphereCenter[2]) + (eyeCoordiantes[0] * eyeCoordiantes[0] ) + (eyeCoordiantes[1] * eyeCoordiantes[1]) + (eyeCoordiantes[2] * eyeCoordiantes[2]) + (-2) * (SphereCenter[0] * eyeCoordiantes[0] + SphereCenter[1] * eyeCoordiantes[1] + SphereCenter[2] * eyeCoordiantes[2]) - (R*R)
        dis = (b*b) - (4 * a * c)
        if dis < 0:
                px = lightSrcCoordinates[0] - x
                py = lightSrcCoordinates[1] - y
                pz = lightSrcCoordinates[2] - z

                ap = (px * px) + (py * py) + (pz * pz)
                bp = 2 * (px) * (x - SphereCenter[0]) + 2 * py *(y - SphereCenter[1]) + 2 * pz * (z - SphereCenter[2])
                cp = (SphereCenter[0] * SphereCenter[0]) +(SphereCenter[1] * SphereCenter[1]) + (SphereCenter[2] * SphereCenter[2]) + (x * x) + (y * y) + (z *z) - (2 * (SphereCenter[0] * x  + SphereCenter[1]* y + SphereCenter[2] * z)) - (R * R)
                disp = (bp * bp) - (4 * ap * cp)
                if disp >= 0:
                    pixels[x,y] = (127, 127, 127)
                else:  
                    pixels[x,y] = (backgroundColor[0], backgroundColor[1], backgroundColor[2]) 
        else:    
            t = (-b - (math.sqrt(dis))) / (2 * a)
            newx = eyeCoordiantes[0] + t * dx
            newy = eyeCoordiantes[1] + t * dy
            newz = eyeCoordiantes[2] + t * dz
            Nx = ((newx - SphereCenter[0]) / R)
            Ny = ((newy - SphereCenter[1]) / R)
            Nz = ((newz - SphereCenter[2]) / R) 
            Norm.append(Nx)
            Norm.append(Ny)
            Norm.append(Nz)
            Lx = lightSrcCoordinates[0] - newx
            Ly = lightSrcCoordinates[1] - newy
            Lz = lightSrcCoordinates[2] - newz
            Lmag = math.sqrt((Lx *Lx) + (Ly * Ly) + (Lz * Lz)) 
            Lx = Lx / Lmag
            LV.append(Lx)
            Ly = Ly / Lmag
            LV.append(Ly)
            Lz = Lz / Lmag
            LV.append(Lz)
            colorambX = ambLight(SphereColor[0], 0.2)
            colorambY = ambLight(SphereColor[1], 0.2)
            colorambZ = ambLight(SphereColor[2], 0.2)
            colordiffX = abs(diffuseReflection(SphereColor[0], 0.8, LV, Norm))
            colordiffY = abs(diffuseReflection(SphereColor[1], 0.8, LV, Norm))
            colordiffZ = abs(diffuseReflection(SphereColor[2], 0.8, LV, Norm))
            colorTotalX = colorambX + colordiffX
            colorTotalY = colorambY + colordiffY
            colorTotalZ = colorambZ + colordiffZ
            pixels[x,y] = (colorTotalX, colorTotalY, colorTotalZ)
            Norm.clear()
            LV.clear()
img.save(filename)
webbrowser.open(filename)