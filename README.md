# ivp-online-proctoring-system
IVP mini project

Dependencies: (command to install : pip install "library")
- imutils
- mediapipe
- cv2

 
Issues:
Traceback (most recent call last):
  File "ops.py", line 41, in <module>
    faces[0].mouth = main_open_mouth(frame, faces)
  File "c:\Users\Anirudh\mini_project_iiita\detect_open_mouth.py", line 35, in main_open_mouth
    mouthMAR = mouth_aspect_ratio(landmarks)
  File "c:\Users\Anirudh\mini_project_iiita\detect_open_mouth.py", line 18, in mouth_aspect_ratio
    B = dist.euclidean(landmarks[267,:], landmarks[314,:]) # 53, 57 # media(267,314)
IndexError: index 314 is out of bounds for axis 0 with size 277
