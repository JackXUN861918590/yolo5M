import time
import zipfile
import shutil
import os.path


def unzip_file(ZipfilePath,TragetPath):
    with zipfile.ZipFile(ZipfilePath,'r') as zip_ref:
        zip_ref.extractall(TragetPath)


unzip_file('photo.zip','./Train')

print("Unzip succefully!")



