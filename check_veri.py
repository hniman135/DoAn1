import os
import shutil
os.system('python camera_check.py')
remove_path = "runs"
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)
os.system('python detect.py --source bienso.png --save-crop')
os.system('python readqr.py')