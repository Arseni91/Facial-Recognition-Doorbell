import os
from os import listdir

def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))

directory = '/home/pi/Desktop/Project'
fles = list_files1(directory, "jpg")
for f in fles:
    print (f)