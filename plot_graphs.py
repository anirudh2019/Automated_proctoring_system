import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def plot_main(frames):
    facedet=[]
    facerec=[]
    head=[]
    mouth=[]
    spoof=[]
    cheat=[]
    for frame in frames:
        facedet.append(frame.facedet)
        facerec.append(frame.facerec)
        head.append(frame.head)
        mouth.append(frame.mouth)
        spoof.append(frame.spoof)
        cheat.append(frame.cheat)
    
    plt.subplot(6,1,1)
    plt.plot(facedet,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Face Detection")
    
    plt.subplot(6,1,2)
    plt.plot(facerec,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Face Recognition")
    
    plt.subplot(6,1,3)
    plt.plot(head,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Head-pose Estimation")
    
    plt.subplot(6,1,4)
    plt.plot(mouth,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Mouth Open Detection")
    
    plt.subplot(6,1,5)
    plt.plot(spoof,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Spoof Detection")
    
    plt.subplot(6,1,6)
    plt.plot(cheat,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Estimated cheat probability")
    plt.show()