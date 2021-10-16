from face_land_mp import face_landmarks_mp
from imutils import face_utils
import numpy as np
import cv2
import dlib
import utils

# Facial landmarks predictor
saved_model = "models/shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(saved_model)

def detect_landmarks(frame, faces, module = "Dlib"):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    real_h, real_w, c = frame.shape
    
    if module == "Dlib":
        # loop over the face detections
        for (i, face) in enumerate(faces):
            x,y,w,h = face.bbox
            l = x if x>=0 else 0
            t = y if y>=0 else 0
            r = x+w if x+w<= real_w else real_w
            b = y+h if y+h<= real_h else real_h
            shape = predictor(gray, dlib.rectangle(l,t,r,b) )
            face.shape = face_utils.shape_to_np(shape)
                
    elif module == "mediapipe":
        ret, face.shape, frame = face_landmarks_mp(frame)

