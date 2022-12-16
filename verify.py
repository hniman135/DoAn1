import pymongo 
from ocr import getStr

path = 'pic_ocr/pic1.jpg'
UpStrg, DownStrg = getStr(path)

numcheck = 973

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client["License_Plate_Manager"]
information = db.table0

result = information.find({"id": numcheck})

for res in result:
    if UpStrg == res["Up"] and DownStrg == res["Down"]:
        print ("ACP!!!")
    else:
        print("NAHHHH")