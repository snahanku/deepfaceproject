from flask import  Flask 
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2
app= Flask(__name__)



app.route("/face")
def faceDetection():
    face=DeepFace.detectFace("templates/rabindranathTagore/Rabi-1.jpg" , target_size=(224 , 224 ), detector_backend="opencv")
    print(face)
    return("face registered ")



app.route("/facematch")
def facematch():
    result=DeepFace.find(img_path='templates/rabindranathTagore/rabi-2.jpg', db_path="templates/")
    print(result)
    return ("ok face matched")




if __name__=="__main__":
    app.run()