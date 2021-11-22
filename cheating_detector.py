class Frame:
    def __init__(self):
        self.cheat = 0
        self.count = 0
        self.cheatcount = 0
        self.noface = 0
        self.multiface = 0
        self.facerec = 0
        self.head = 0
        self.eye = 0
        self.mouth = 0
        self.spoof = 0

class Segment:
    def __init__(self):
        self.cheat = 0
        self.count = 0
        self.cheatcount = 0

def detect_cheating_frame(faces,frames):

    frame=Frame()
    bool_flag=0
    if faces:
        if(len(faces)!=1):
            frame.multiface = 1
            bool_flag+=1

        for face in faces:
            if face.name=="Unknown":
                frame.facerec=1
                bool_flag+=1
            
            if not face.spoof:
                frame.spoof = 1
                bool_flag+=1

            if face.head!="Head Straight":
                frame.head=1
                bool_flag+=1

            if face.mouth:
                if face.mouth.status=="mouth open":
                    frame.mouth=1
                    bool_flag+=1
    else:
        frame.noface = 1
        bool_flag+=1

    if(bool_flag>0):
        frame.cheat = 1
        frame.cheatcount = bool_flag
    else:
        frame.cheat = 0
        frame.cheatcount = 0

    frame.count=len(frames)+1
    return frame

def segment_count(frames):
    # count variables
    frame_count = 0
    segment_count=0
    cheat_segment_count=0
    noface_cheat_count = 0
    multiface_cheat_count = 0
    facerec_cheat_count = 0
    head_cheat_count = 0
    mouth_cheat_count = 0
    spoof_cheat_count = 0
    segment_time = 10#20
    fps_assumed = 5

    # thresholds
    noface_cheat_threshold = 60
    multiface_cheat_threshold = 60
    facerec_cheat_threshold = 30
    head_cheat_threshold = 30
    mouth_cheat_threshold = 30
    spoof_cheat_threshold = 30

    segments = []
    for frame in frames:
        frame_count+=1
        if(frame.noface):
            noface_cheat_count+=1
        if(frame.multiface):
            multiface_cheat_count+=1
        if(frame.facerec):
            facerec_cheat_count+=1
        if(frame.head):
            head_cheat_count+=1
        if(frame.mouth):
            mouth_cheat_count+=1
        if(frame.spoof):
            spoof_cheat_count+=1
        

        if(frame_count)%(segment_time*fps_assumed)==0:
            seg = Segment()
            seg.count = segment_count
            segment_count+=1
            seg.cheat = cheat_segment_count
            cheat_segment_count=0
            #print(segment)
            segments.append(seg)

            if((noface_cheat_count>=noface_cheat_threshold) or (multiface_cheat_count>=multiface_cheat_threshold) or (facerec_cheat_count>=facerec_cheat_threshold) or (head_cheat_count>=head_cheat_threshold) or (mouth_cheat_count>=mouth_cheat_threshold) or (spoof_cheat_count>=spoof_cheat_threshold)):
                cheat_segment_count+=1

            noface_cheat_count = 0
            multiface_cheat_count = 0
            spoof_cheat_count = 0
            head_cheat_count = 0
            mouth_cheat_count = 0
            
    return segments

def print_stats(segments):
    cheat_count =0
    for segment in segments:
        if(segment.cheat):
            cheat_count+=1
    print("\n*****************************\n")
    print("segment_count = ", len(segments))
    print("cheatings observed  = ", cheat_count)
    print("\n*****************************\n")

