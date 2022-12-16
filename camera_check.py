import pymongo 
import cv2
import pyqrcode
from ocr import getStr

#path = 'pic_ocr/pic1.jpg'
cam = cv2.VideoCapture(0)
result, image = cam.read()
if result:
  
    # showing result, it take frame name and image 
    # output
    #cv2.imshow("bienso", image)
  
    # saving image in local storage
    cv2.imwrite("popBike.png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    cv2.waitKey(0)
    cam.release()
    #cv2.destroyWindow("bienso")

else:
    print("No image detected. Please! try again")


