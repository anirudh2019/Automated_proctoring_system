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
1. First download this project. We used anaconda environments to manage dependencies for this project, so download anaconda installer from [here](https://www.anaconda.com/products/individual#Downloads).
2. Installing Microsoft C++ Build Tools:
2.1. Download Microsoft C++ Build Tools from [here](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2.2. Run the downloaded setup. 
2.3. When the following window appears, tick “Desktop development with C++” as shown and make sure that the below shown ones are also ticked. Now click on install.
xxxxxxx
3. Now download proctorenv.yml from readme folder of this repository. 
4. Open anaconda prompt and go to the directory where proctorenv.yml is there.
5. Type in anaconda prompt: conda env create -f proctorenv.yml
6. Now a conda environment called "proctorenv" is created. To activate this env, type: conda activate proctorenv
7. After activating proctorenv env, go to the directory which has main.py of this project. Type: python main.py to start the proctoring system.
8. First register yourself on the first screen by pressing `r` to capture you images for 5 times.
9. Now proctoring will begin and it will end after you press the `esc` key.
10. The reports generated will be stored in the `./results` folder.
