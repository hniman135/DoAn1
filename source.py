import os
import shutil
os.system('python camera.py')
remove_path = "runs"
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)
os.system('python detect.py --source GeeksForGeeks.png --save-crop')
os.system('python ocr.py')
os.system('python import_data.py')