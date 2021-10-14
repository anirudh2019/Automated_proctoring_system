import cv2
from face_land_mp import face_landmarks_mp

def mouth_main(img, shape):
    
    outer_points = [[49, 59], [50, 58], [51, 57], [52, 56], [53, 55]]
    d_outer = [0]*5
    inner_points = [[61, 67], [62, 66], [63, 65]]
    d_inner = [0]*3
    font = cv2.FONT_HERSHEY_SIMPLEX 
    # alert_bool, shape, img2 = face_landmarks_mp(face)
    #cv2.putText(img, 'Press r to record Mouth distances', (30, 30), font, 1, (0, 255, 255), 2)
    for i in range(100):
        for i, (p1, p2) in enumerate(outer_points):
            d_outer[i] += shape[p2][1] - shape[p1][1]
        for i, (p1, p2) in enumerate(inner_points):
            d_inner[i] += shape[p2][1] - shape[p1][1]
    d_outer[:] = [x / 100 for x in d_outer]
    d_inner[:] = [x / 100 for x in d_inner]
    cnt_outer = 0
    cnt_inner = 0
    
    for i, (p1, p2) in enumerate(outer_points):
        if d_outer[i] + 3 < shape[p2][1] - shape[p1][1]:
            print('x')
            cnt_outer += 1 
    for i, (p1, p2) in enumerate(inner_points):
        if d_inner[i] + 2 <  shape[p2][1] - shape[p1][1]:
            print('y')
            cnt_inner += 1
    if cnt_outer > 3 and cnt_inner > 2:
        print('Mouth open')
        cv2.putText(img, 'Mouth open', (30, 30), font, 1, (0, 255, 255), 2)
    print(cnt_outer, cnt_inner)
    return img