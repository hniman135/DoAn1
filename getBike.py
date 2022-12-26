import os
import shutil

remove_path = "runs"
crop_path = "runs/detect/exp/crops"
if os.path.exists(remove_path):
        shutil.rmtree(remove_path)

while (os.path.exists(crop_path) == False):
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    os.system('python camera.py')
    os.system('python detect.py --source getBike.png --save-crop')

    os.system('python import_data.py')
