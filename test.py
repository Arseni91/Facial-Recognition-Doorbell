import os
import dlib
from skimage import io
from scipy.spatial import distance
#os.system("raspistill -w 640 -h 480 -o tesst.jpg")
print("Image done") 
sp = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
facerec=dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()

face_descriptor1 = None
#face_descriptor2 = None



img = io.imread('Ela.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor1 = facerec.compute_face_descriptor(img, shape)

	
f = open("demofile.txt", "w")
f.write(face_descriptor1) 
'''
img = io.imread('tesst1.jpg')
dets = detector(img, 0)
for k, d in enumerate(dets):
    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        k, d.left(), d.top(), d.right(), d.bottom()))
    shape = sp(img, d)
face_descriptor2 = facerec.compute_face_descriptor(img, shape)


a = distance.euclidean(face_descriptor1, face_descriptor2)
print(a)
'''