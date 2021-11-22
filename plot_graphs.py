import numpy as np
import time 
import matplotlib.pyplot as plt

def plot_main(frames):
    noface=[]
    multiface=[]
    facerec=[]
    head=[]
    mouth=[]
    spoof=[]
    cheat=[]
    for frame in frames:
        noface.append(frame.noface)
        multiface.append(frame.multiface)
        facerec.append(frame.facerec)
        head.append(frame.head)
        mouth.append(frame.mouth)
        spoof.append(frame.spoof)
        cheat.append(frame.cheat)
    
    plt.figure(figsize=(12,20)) 
    
    plt.subplot(7,1,1)
    plt.plot(noface,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Absence of Face")

    plt.subplot(7,1,2)
    plt.plot(multiface,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Multiple faces")
    
    plt.subplot(7,1,3)
    plt.plot(facerec,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Unauthenticated user")
    
    plt.subplot(7,1,4)
    plt.plot(head,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Staring away from screen")
    
    plt.subplot(7,1,5)
    plt.plot(mouth,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Talking")
    
    plt.subplot(7,1,6)
    plt.plot(spoof,color='red')
    # plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Spoof Detection")
    
    plt.subplot(7,1,7)
    plt.plot(cheat,color='red')
    plt.xlabel('frames') 
    plt.ylabel('cheat status')
    plt.title("Estimated cheat probability")

    plt.subplots_adjust(hspace = 1.0)
    plt.savefig("results/cheat_frames_"+ time.strftime("%Y%m%d-%H%M%S") + ".png",dpi=300)
    plt.show()

def cheat_count(segments):
    cheat_count =0
    for segment in segments:
        if(segment.cheat):
            cheat_count+=1
    return cheat_count

def plot_segments(segments):
    x=[]
    y=[]
    n = cheat_count(segments)
    for segment in segments:
        x.append(segment.count)
        y.append(segment.cheat)

    fps_assumed = 5
    segment_time = 10
    
    plt.figure(figsize=(12,4)) 
    plt.plot(x,y,'r')
    plt.xlabel('Time Segments')
    plt.ylabel('Cheating Suspect Count')
    stats = "Total Time : " + str(len(segments)*segment_time) + " seconds\n" + "Cheating Suspected for : " + str(n*segment_time) + " seconds"
    plt.figtext(0.5, 0.9,stats, ha="center", fontsize=12, bbox={"facecolor":"orange", "alpha":0.5, "pad":3})
    plt.savefig("results/cheating_detection_"+ time.strftime("%Y%m%d-%H%M%S") + ".png",dpi=300)
    plt.show()

