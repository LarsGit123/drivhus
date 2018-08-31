from imgproc import *
import cv2 as cv
import numpy as np
filepath='/home/pi/webcam/'



def GetImage(imageName):
    img= cv.imread(imageName)
    return img
    
def GetMaxXY(img):
    maxIntensity=0.0
    height, width, channels = img.shape
    for x in range(0,width,10):
        for y in range(0,height-100,10):
            red=float(img[y,x,0])
            blue=float(img[y,x,1])            
            green=float(img[y,x,2])
            intensity=round(np.cbrt(red*green*blue),2)
            if intensity>maxIntensity:
                maxIntensity=intensity
                MaxXY=[y, x]
    return MaxXY

def GetAvgIntensity(img, MaxXY):
    height, width, channels = img.shape
    counter=0.0
    avgIntensity=0.0
    for x in range(0, width,10):
        counter=counter+1.0
        red=float(img[MaxXY[0],x,0])
        blue=float(img[MaxXY[0],x,1])            
        green=float(img[MaxXY[0],x,2])
        intensity=round(np.cbrt(red*green*blue),2)
        avgIntensity+=intensity

    avgIntensity=round(avgIntensity/counter,2)
    print("AvgIntensity.  "+str(avgIntensity))
    return avgIntensity
        
def GetAndSaveFocusImg(img, MaxXY, filename):
    height, width, channels = img.shape
    xrangeMin=MaxXY[1]-150
    if(xrangeMin<0):
        xrangeMin=0

    xrangeMax=MaxXY[1]+150
    if(xrangeMin>width):
        xrangeMin=width

    yrangeMin=MaxXY[0]-150
    if(yrangeMin<0):
        yrangeMin=0

    yrangeMax=MaxXY[0]+150
    if(yrangeMin>height):
        yrangeMin=height    

    print( str(yrangeMin)+" " +str(yrangeMax) + " "+str(xrangeMin)+" " +str(xrangeMax))
    focus =img[yrangeMin:yrangeMax,xrangeMin:xrangeMax]
    cv.imwrite(filename+'_Focus',focus)

    
