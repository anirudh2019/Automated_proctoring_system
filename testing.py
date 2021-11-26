def time_to_frame(x,fps):
    minn = int(x[:2])
    sec = int(x[2:])
    no_frames = (minn*60+sec)*fps
    return no_frames

def input_data(data_path):
    data_file = open(data_path, "r")
    input_text = data_file. readlines()
    input_frwise_text = []
    fps,video_length = int(input_text[0].strip("\n")),int(input_text[1].strip("\n"))
    for ch_inst in input_text[2:]:
        start_f, end_f, tag = tuple(ch_inst.strip("\n").split(" "))
        start_f = time_to_frame(start_f, fps)
        end_f = time_to_frame(end_f,fps)
        input_frwise_text.append([start_f, end_f, tag])
    return fps,video_length,input_frwise_text

def testing_accuracy(data_path,segment_size=25):
    fps,video_length,input_text = input_data(data_path)
    total_frames = fps*video_length
    no_of_segments = total_frames/segment_size
    original = [0]*int(no_of_segments)

    for i in range(len(input_text)):
        a=input_text[i][0]/segment_size #START FRAME  
        b=input_text[i][1]/segment_size #END FRAME
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
    
    # if tp>0 and tn>0 and fp>0 and fn >0:
    #     accuracy = (tp+tn)/(tp+fp+fn+tn)
    #     precision = tp/(tp+fp)
    #     recall = tp/(tp+fn)
    #     f1score = 2*(precision*recall)/(precision+recall)
    #     print(f"Accuracy = {accuracy}\n Precision = {precision}\n Recall = {recall}\n F1Score = {f1score}")
    #     return accuracy,precision,recall,f1score
    # else:
    #     return 0,0,0,0

    accuracy = (tp+tn)/(tp+fp+fn+tn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1score = 2*(precision*recall)/(precision+recall)
    print(f"Accuracy = {accuracy}\n Precision = {precision}\n Recall = {recall}\n F1Score = {f1score}")
    return accuracy,precision,recall,f1score
    