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
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from gpiozero import LED
from kivy.clock import Clock
clicked = False
def cl():
    clicked = False
led = LED(21)
led1 = LED(20)
sp = dlib.shape_predictor('/home/pi/Desktop/Project/shape_predictor_68_face_landmarks.dat')
facerec=dlib.face_recognition_model_v1('/home/pi/Desktop/Project/dlib_face_recognition_resnet_model_v1.dat')
detector = dlib.get_frontal_face_detector()
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
	
	
#Config.set('graphics', 'width', '480')
#Config.set('graphics', 'height', '320')
Config.set('graphics', 'fullscreen', 'auto')
Config.set('graphics', 'window_state', 'maximized')
Config.write()

def callback(instance):
    if(instance.text=="Press Here"):        
        instance.text = "Waiting";
    
        face_descriptortest = None
        os.system("raspistill -w 640 -h 480 -o /home/pi/Desktop/Project/img/tesst.jpg")
        img = io.imread('/home/pi/Desktop/Project/img/tesst.jpg')
        dets = detector(img, 0)
        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
            shape1 = sp(img, d)
            face_descriptortest = facerec.compute_face_descriptor(img, shape1)
            print("Found face")
        signal = "Access Denied.jpg"
        dist = 1
        if(face_descriptortest!=None):
            signal = "Access Denied"	        
            disttemp=1
            temp = None
            for fd in dict:
                print(dict[fd])
                disttemp=distance.euclidean(fd, face_descriptortest)
                if(disttemp<dist and disttemp<0.6):
                    dist=disttemp
                    temp=fd
                if(temp!=None):
                    signal = dict[temp]
        signal = signal[:-4]+" on "+time.strftime("%H:%M:%S")
        instance.text = signal
    
        sent_from = 'facerecongproject2018@gmail.com' 
        to = 'facerecongproject2018@gmail.com'     
        try:
            img_data = open('/home/pi/Desktop/Project/img/tesst.jpg', 'rb').read()
            outer = MIMEMultipart()
            outer['Subject'] = signal
            outer['From'] = sent_from
            outer['To'] = to
            #text = MIMEText("test")
            body=signal
            fp = open('/home/pi/Desktop/Project/img/tesst.jpg', 'rb')
            msg1 = MIMEImage(fp.read(),'jpg')
            fp.close()
            filename = 'tesst.jpg'
            outer.add_header('Content-Disposition', 'attachment', filename=filename)
            outer.attach(msg1)
            text = outer.as_string()
            
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()  
            server_ssl.login("facerecongproject2018", "Face4321")
            server_ssl.sendmail("facerecongproject2018@gmail.com", "facerecongproject2018@gmail.com", text)
            server_ssl.close()
        except Exception:
            pass
        print("Finish")
        print(signal)
        if(dist>0.6):
            led.on()
            sleep(5)
            led.off()
        else:        
            led1.on()
            sleep(5)
            led1.off()
    #instance.text = "Press Here"
button1 = Button(text='Press Here', font_size=36)
button1.bind(on_press=callback)


def check_ping():
    hostname = "taylor"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = True
    else:
        pingstatus = False
    return pingstatus

class TestApp(App):
    def build(self):
        Clock.schedule_interval(self.timer, 50)
        self.button = button1
        self.check  = clicked
        return self.button
    def timer(self, dt):
        clicked = False
        self.button.text = "Press Here"
TestApp().run()