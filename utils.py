import cv2
import time
import numpy as np

from face_detection import detect_faces
font = cv2.FONT_HERSHEY_PLAIN 

def convert_bbox(bbox, small_frame): ## from relative bbox to css order
    real_h, real_w, c = small_frame.shape
    x,y,w,h = bbox
    y1 = 0 if y < 0 else y
    x1 = 0 if x < 0 else x 
    y2 = real_h if y1 + h > real_h else y + h
    x2 = real_w if x1 + w > real_w else x + w
    return (y1, x2, y2, x1)

def print_fps(frame, pTime):
    cTime = time.time()
    fps = 1/(cTime - pTime[0])
    pTime[0] = cTime
    cv2.putText(frame, f"fps : {int(fps)}", (30,30),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    return frame

def print_faces(frame, faces):
    for face in faces:
        cv2.rectangle(frame, face.bbox, (0, 0, 255), 2)
        cv2.putText(frame, 'name : ' + face.name, (30,60),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
        cv2.putText(frame, 'dist : ' +str(face.distance), (30,90),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
    return frame
    

def register_user(fr, num_pics = 5):  # Here model is Face_recogntion model
    user_name = input("Please enter your name: ")
    cam = cv2.VideoCapture(0)
    cv2.namedWindow('Face registration')
    count = 0
    input_embeddings = {}
    
    while count<num_pics:  
        ret, frame = cam.read()
        if ret:
            cv2.putText(frame, 'Press r to capture image, {}/{} captures done'.format(count,num_pics),(30,60),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0),2)
            cv2.imshow('Face registration', frame)
        
            if cv2.waitKey(1) & 0xFF == ord('r'):
                # capturing image 
                alert, faces =  detect_faces(frame, confidence = 0.7)
                if alert:
                    print('No face detected or Multiple faces detected. Please try again.')
                else:
                    face_img = faces[0].img
                    input_embeddings[user_name] = fr.face_to_embedding(face_img)
                    count+=1
                    # saving image as use_image.jpg for further face verification
                    cv2.imwrite("captures/{}_{}.jpg".format(user_name, count), face_img)
        else:
#             print("Camera not available, close any other apps using the webcam and try again")
            continue    
    cam.release()
    cv2.destroyAllWindows()
    
    return input_embeddings