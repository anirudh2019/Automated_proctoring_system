import numpy as np
import cv2
import sys
from face_detection import detect_faces
from face_recog import Recognizer
from face_land import detect_landmarks
from headpose import head_main
from eye_tracker import eye_tracking
from detect_open_mouth import main_open_mouth
from face_spoofing import spoof_detector
import utils

font = cv2.FONT_HERSHEY_PLAIN 
pTime = [0]


# Face recognizer
fr = Recognizer(threshold = 0.8)

# Register User
fr.input_embeddings = utils.register_user(fr, num_pics = 5)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('PROCTORING ON')

    while(True):
        ret, frame = cap.read()
        frame = utils.print_fps(cv2.flip(frame, 1), pTime)
        
        det_alert, faces =  detect_faces(frame, confidence = 0.7)
        
        if det_alert!="No face": 
            fr.verify_faces(faces)
            spoof_detector(faces)
            detect_landmarks(frame, faces, module="Dlib")
            if not det_alert:
                head_main(frame,faces[0].shape)
                eye_tracking(frame, faces[0].shape, threshold = 75)
                main_open_mouth(frame, faces[0].shape)
                
        frame = utils.print_faces(frame, faces)        
        
        cv2.imshow('PROCTORING ON',  frame)
                
        if cv2.waitKey(1) & 0xFF == 27: 
            break
    cap.release()
    cv2.destroyAllWindows()


#    DO NOT DELETE THIS!
# Warnings in head pose estimation:
#     C:\Users\Anirudh\mini_project_iiita\headpose.py:129: RuntimeWarning: divide by zero encountered in int_scalars
#   m = (x2[1] - x1[1])/(x2[0] - x1[0])
#   ang2 = ...(1/m)..
# C:\Users\Anirudh\mini_project_iiita\eye_tracker.py:39: RuntimeWarning: divide by zero encountered in long_scalars
#   y_ratio = (cy - end_points[1])/(end_points[3] - cy)

# Rough:
        # outputs: detreg_out, landeye_out, head_out
#         head_out = cv2.copyMakeBorder(head_out, 0, 0, 320, 320, cv2.BORDER_CONSTANT, (0,0,0))
#         horiz = np.concatenate((horiz, head_out), axis = 1)