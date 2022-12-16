import cv2 #Read image / camera/video input
from pyzbar.pyzbar import decode
import time
from ocr import getStr
import pymongo
import bson
cap = cv2. VideoCapture (0)
camera = True
while camera == True:
    success, frame = cap.read ()
    for code in decode (frame):
        qr_dectect = code.data.decode ('utf-8')
        camera = False

id = bson.objectid.ObjectId(qr_dectect)

path = 'runs/detect/exp/crops/bienso/popBike.jpg'
UpStrg, DownStrg = getStr(path)
print(UpStrg, DownStrg)


client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client["License_Plate_Manager"]
information = db.table0


  
# If image will detected without any error, 
# show result
result = information.find({'_id' : id})
for res in result:

    if UpStrg == res["Up"] and DownStrg == res["Down"]:
        acp = 1
    else:
        acp = 0
print(acp)





