import os
import shutil
crop_path = "runs/detect/exp/crops"
remove_path = "runs"
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)
while (os.path.exists(crop_path) == False):
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    os.system('python camera_check.py')
    os.system('python detect.py --source popBike.png --save-crop')
os.system('python readqr.py')