import os
import datetime
import time
import dlib
from time import sleep
from skimage import io
from scipy.spatial import distance
from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from os import listdir

def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))	
	
dict={}
directory = '/home/pi/Desktop/Project'
fles = list_files1(directory, "jpg")

for f in fles:
    face_descriptorTemp= None
    img = io.imread('/home/pi/Desktop/Project/' +f)
    dets = detector(img, 0)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
    face_descriptorTemp = facerec.compute_face_descriptor(img, shape)
    dict[face_descriptorTemp]=f
	
	
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '320')

sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec=dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

face_descriptor1 = None
face_descriptor2 = None
face_descriptor3 = None
face_descriptor4 = None
face_descriptor5 = None


'''
img = io.imread('/home/pi/Desktop/Project/tesst1.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor1 = facerec.compute_face_descriptor(img, shape)

img = io.imread('/home/pi/Desktop/Project/Noa1.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor2 = facerec.compute_face_descriptor(img, shape)

img = io.imread('/home/pi/Desktop/Project/Ela.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor3 = facerec.compute_face_descriptor(img, shape)

img = io.imread('/home/pi/Desktop/Project/Eli.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor4 = facerec.compute_face_descriptor(img, shape)

img = io.imread('/home/pi/Desktop/Project/Ars.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor5 = facerec.compute_face_descriptor(img, shape)
'''
def callback(instance):
    instance.text = "Waiting";	
    face_descriptortest = None
    os.system("raspistill -w 640 -h 480 -o /home/pi/Desktop/Project/tesst.jpg")
    img = io.imread('tesst.jpg')
    dets = detector(img, 0)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
        shape1 = sp(img, d)
        face_descriptortest = facerec.compute_face_descriptor(img, shape1)
    signal = "Deny"	
    dist = 1;
    disttemp=1;
    temp = None
    for fd in dict:
        disttemp=distance.euclidean(fd, face_descriptortest)
        if(disttemp<dist):
            dist=disttemp
            temp=fd
        if(temp!=None):
            signal = dict[temp]	
        print(signal)
	
button = Button(text='Check', font_size=14)
button.bind(on_press=callback)


class TestApp(App):
    def build(self):
        return button

TestApp().run()