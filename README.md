# Robust Automated Proctoring System for Online Examinations

IVP mini project

- This light weight application proctors examinee continuously throughout the exam using webcam and detects several methods of cheating with high accuracy and makes report of their cheating behaviour. 
- It has modules like Face detection, Face recognition, Face landmarks detection, Head pose estimation, Eye gaze detection, Face spoof detection and Lips tracker.
- This application uses less cpu and RAM because we used robust and light weight models like BlazeFace face detector, FaceNet for face recogntion.
- Our application detects the following cheating methods:
  1. Another person giving exam
  2. Another person helping by sitting beside or talking in the same camera frame
  3. Student going away from device abnormal number of times
  4. Student talking to someone (including on phone)
  5. Student staring away from screen abnormal number of times (staring out of screen, staring down for accessing mobile or a book)
  6. Student spoofing his presence
- **Results:**
Our proctoring system has scored 96.22% accuracy on our test dataset.
- A glimpse of live proctoring on test dataset:<br><br>
![image](https://github.com/anirudh2019/IML-2021/blob/main/live.png?raw=true)
![image](https://github.com/anirudh2019/IML-2021/blob/main/1.jpg?raw=true)
![image](https://github.com/anirudh2019/IML-2021/blob/main/2.jpg?raw=true)



Instructions to run this project:
1. we used anaconda environments to manage dependencies for this project so to begin with download anaconda installer from [here](https://www.anaconda.com/products/individual#Downloads) .
2. create a new environment and install the following dependent python libraries in the new environment using `conda` or `pip` as `pip install "libraryname"` for the following libraries.

```
cmake
scipy
opencv
dlib
imutils
mediapipe
tensorflow==2.6.0
```

YOU COULD DO SAME USING A `virtualenv` using python 3.7+\*

3. Now run the main function in the source code as `python main.py` to start the proctoring system.
4. First register yourself on the first screen by pressing `r` to capture you images for 5 times.
5. Now monitoring will begin and it will end after you press the `esc` key .

6. The reports generated will be stored in the `./results` folder.
