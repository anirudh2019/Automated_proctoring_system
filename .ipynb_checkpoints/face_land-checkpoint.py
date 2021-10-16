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

def detect_landmarks(frame, faces, module = "Dlib", draw=True):
    shape = []
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # rects = detector(gray, 0)
    if module == "Dlib":
        # loop over the face detections
        for (i, face) in enumerate(faces):
            # determine the facial landmarks for the face region, then
            # convert the facial landmark (x, y)-coordinates to a NumPy
            # array
            shape = predictor(gray, dlib.rectangle(face.bbox[0], face.bbox[1], face.bbox[0]+face.bbox[2], face.bbox[1]+face.bbox[3]))
            shape = face_utils.shape_to_np(shape)
        
            # loop over the (x, y)-coordinates for the facial landmarks
            # and draw them on the frame
            if draw:
                for (x, y) in shape:
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)      
    elif module == "mediapipe":
        ret, shape, frame = face_landmarks_mp(frame)
    
    return True, shape, frame