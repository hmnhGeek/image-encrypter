from PIL import Image
import os

def isimage(f):

    try:
        Image.open(f)
    except:
        return False
    return True

def findallimages(directory):

    cwd = os.getcwd()
    
    os.chdir(directory)

    files = [f for f in os.listdir('.')]
    images = []

    for f in files:
        if isimage(f):
            images.append(f)

    os.chdir(cwd)

    return images

def findallbinaries(directory):

    cwd = os.getcwd()
    
    os.chdir(directory)

    files = []

    for f in os.listdir('.'):
        if f.endswith('.gz'):
            files.append(f)

    os.chdir(cwd)

    return files
