import pymongo
import pyqrcode
import time
from ocr import getStr

client = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = client['License_Plate_Manager']

information = mydb.table0

path = 'runs/detect/exp/crops/bienso/GeeksForGeeks.jpg'
UpStrg, DownStrg = getStr(path)

sec = time.time()

rec= [{
    "time" : sec,
    "Up" : UpStrg,
    "Down": DownStrg
    }]
information.insert_many(rec)

id = information.find({'time' : sec})
for i in id:
    input_data =str(i["_id"])

qr = pyqrcode.create(input_data)

qr.show()