import os

from pathlib import Path 
from Getdir.getdirs import Dir
from Getdir.uniquelist import unique


dirsList = []
tempDir = Dir().get_temp_dir
# tempDir = r'C:\Users\sammy\Desktop'

def delete_temp(tempDir):
    for roots, dirs, files in os.walk(tempDir):
        print("Root: {} \n\n\n Dir:{} \n\n\n Files:{}".format(roots, dirs, files))
        if files:
            for file in files:
                pathfile = os.path.join(roots, file)
                os.remove(pathfile)
        if dirs:
            for dir in dirs:
                dirPath = os.path.join(roots, dir)
                dirsList.append(dirPath)


    for dir in dirsList:
        if dir is tempDir:
            continue
        else:
            try:
                Path(dir).rmdir()
            except OSError:
                continue

    for dir in reversed(dirsList):
        if dir is tempDir:
            continue
        else:
            try:
                Path(dir).rmdir()
            except OSError:
                continue



if __name__ == "__main__":
    delete_temp(tempDir)