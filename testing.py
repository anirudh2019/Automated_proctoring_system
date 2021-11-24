def time_to_frame(x,fps):
    minn = int(x[:2])
    sec = int(x[2:])
    no_frames = (minn*60+sec)*fps
    return no_frames

def input_data(data_path, fps):
    data_file = open(data_path, "r")
    input_text = data_file. readlines()
    input_frwise_text = []
    for ch_inst in input_text:
        start_f, end_f, tag = tuple(ch_inst.strip("\n").split(" "))
        start_f = time_to_frame(start_f, fps)
        end_f = time_to_frame(end_f,fps)
        input_frwise_text.append([start_f, end_f, tag])
    return input_frwise_text


#print(input_data("data.txt",15))

def testing_accuracy(length_of_video = 300,fps_of_video = 20,fps_assumed = 5,segment_time = 5,input_text=[]):
    total_frames = length_of_video*fps_of_video #600
    segment_length = segment_time*fps_assumed #no of frames in a segment
    no_of_segments = total_frames/segment_length
    original = [0]*int(no_of_segments)

    for i in range(len(input_text)):
        a=input_text[i][0]/segment_length #START FRAME 0130 90 1 1 1800 72 
        b=input_text[i][1]/segment_length #END FRAME 0204 124 1 1 2480 89
        for j in range(int(a),int(b)+1):
            original[j]=1
    return original

def detected_cheating(segments):
    detected = []
    for segment in segments:
        detected.append(segment.cheat)
    return detected


def get_accuracy(original,detected):
    fp = 0
    tp = 0
    fn = 0
    tn = 0
    for i in range(min(len(original),len(detected))):
        if original[i]==0 and detected[i] ==0:
            tn+=1
        elif original[i]==1 and detected[i] ==0:
            fn+=1
        elif original[i]==0 and detected[i] ==1:
            fp+=1
        elif original[i]==1 and detected[i] ==1:
            tp+=1
    accuracy = (tp+tn)/(tp+fp+fn+tn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1score = 2*(precision*recall)/(precision+recall)
    print(f"Accuracy = {accuracy}\n Precision = {precision}\n Recall = {recall}\n F1Score = {f1score}")
    return accuracy,precision,recall,f1score