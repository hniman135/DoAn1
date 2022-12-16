import easyocr
import cv2
import numpy as np
import glob
import os
import sys
import shutil
#delete folder
    #@check if the dicrectory exist, deleted it
remove_path = "C:/Users/manax/Source/EasyOCR/Resized_Folder"
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)


#resize image folder

    #@create a folder that contain Resized image 
'''
inputFolder = 'pic_ocr' 
os.mkdir('Resized_Folder')
    #@create a reader ocr
reader = easyocr.Reader(['en'])
i=0
for img in glob.glob(inputFolder + "/*.jpg"): #read image that type .jpg
    image = cv2.imread(img)
    imgResized = cv2.resize(image, (500, 500)) #resize image 500x500
    cv2.imwrite("Resized_Folder/image%04i.jpg" %i, imgResized) #save resized image to Resized Folder and rename it
    i +=1
    ocr_results = reader.readtext(imgResized)
    for detection in ocr_results: #read ocr result (top left, bottom right of the rectangle; and it content)
        top_left = [int(value) for value in detection[0][0]] 
        bottom_right = [int(value) for value in detection[0][2]]
        text = detection[1]
        imgResized = cv2.rectangle(imgResized, top_left, bottom_right, (0,0,255), 5)
        imgResized = cv2.putText(imgResized, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2, cv2.LINE_AA)
    cv2.imshow("img", imgResized)
    cv2.waitKey(0)
'''

def main():
    path = 'GeeksForGeeks.png'
    UpStr, DownStr = getStr(path)
    print(UpStr, DownStr)


def getStr(data):  
    reader = easyocr.Reader(['en'])
    ocr_results = reader.readtext(data, allowlist = '0123456789ABCDEFGHIKLMNOPQRSTUVWXYZ')
    return ocr_results[0][1], ocr_results[1][1]


if __name__ == "__main__":
    main()