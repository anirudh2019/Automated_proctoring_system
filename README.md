# Robust Automated Proctoring System for Online Examinations

<h2>IVP mini project</h2>

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
<h3>Results:</h3>
Our proctoring system has scored 96.22% accuracy on our test dataset.
<br>A glimpse of live proctoring on test dataset:<br><br>
<img src="https://github.com/anirudh2019/ivp_proctoring_system/blob/main/readme/live.png" alt="live.jpg">
<img src="https://github.com/anirudh2019/ivp_proctoring_system/blob/main/readme/1.jpg" alt="1.jpg">
<img src="https://github.com/anirudh2019/ivp_proctoring_system/blob/main/readme/2.jpg" alt="2.jpg">



<h3>Instructions to run this project:</h3>
<ol>
  <li>First download this project. We used anaconda environments to manage dependencies for this project, so download anaconda installer from <a href="https://www.anaconda.com/products/individual#Downloads">here</a>.</li>
  <li>Installing Microsoft C++ Build Tools:
    <ul>
      <li>Download Microsoft C++ Build Tools from <a href="https://visualstudio.microsoft.com/visual-cpp-build-tools/">here</a>.</li>
      <li>Run the downloaded setup. </li>
      <li>When the following window appears, tick “Desktop development with C++” as shown and make sure that the below shown ones are also ticked. Now click on install.</li>
    </ul><br>
    <img src="https://github.com/anirudh2019/ivp_proctoring_system/blob/main/readme/install1.jpg" alt="install1.jpg">
  </li> 
  <li>Open anaconda prompt and go to the readme directory of this project where proctorenv.yml is there.</li>
  <li>Type in anaconda prompt: conda env create -f proctorenv.yml</li>
  <li>Now a conda environment called "proctorenv" is created. To activate this env, type: conda activate proctorenv</li>
  <li>After activating proctorenv env, go to the directory which has main.py of this project. Type: python main.py to start the proctoring system.</li>
  <li>First register yourself on the first screen by pressing `r` to capture you images for 5 times.</li>
  <li>Now proctoring will begin and it will end after you press the `esc` key.</li>
  <li>The reports generated will be stored in the `./results` folder.</li>
</ol>
