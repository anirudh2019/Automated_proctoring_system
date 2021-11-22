import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Face detection
from face_detector import detect_faces
# Face landmarks detection
from face_landmarks import detect_landmarks
# Face recognition
from face_recognition import verify_faces
from models.Facenet512 import loadFaceNet512Model
# Other Face modules
from face_spoofing import spoof_detector
from head_pose import headpose_est
from mouth_detector import mouth_open
# Cheat predicting modules
from cheating_detector import *
from plot_graphs import *
# Utils
import cv2
from utils import register_user, print_fps, print_faces


font = cv2.FONT_HERSHEY_SIMPLEX 
pTime = [0]
fps_assumed = 5
segment_time = 5

# Register User
frmodel = loadFaceNet512Model()
input_embeddings, input_im_list = register_user(frmodel, num_pics = 1)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('PROCTORING ON')
    frames=[]
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret :
            break

        print_fps(frame, pTime)

        faces =  detect_faces(frame, confidence = 0.7)
        detect_landmarks(frame, faces, det_conf = 0.7, track_conf = 0.7)
        verify_faces(faces, frmodel, input_embeddings)
        spoof_detector(faces)        
        headpose_est(frame, faces)
        mouth_open(faces)

        print_faces(frame, faces)

        cheat_temp = detect_cheating_frame(faces,frames)
        frames.append(cheat_temp)
        if cheat_temp.cheat>0:
            cv2.putText(frame, "Cheating suspected", (15,130), font, 0.5, (0,0,255),2)

        cv2.imshow('PROCTORING ON',  frame)
        if cv2.waitKey(1) & 0xFF == 27: 
            break


    cap.release()
    cv2.destroyAllWindows()

    plot_main(frames,segment_time,fps_assumed)
    segments = segment_count(frames,segment_time,fps_assumed)
    print_stats(segments)
    plot_segments(segments,segment_time)