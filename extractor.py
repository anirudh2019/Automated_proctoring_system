import cv2
import numpy as np

class MouthShape:
    def __init__(self):
        self.outer_bottom = {}
        self.outer_top = {}
        self.inner_bottom = {}
        self.inner_top = {}
        
def get_mouth_points(shape):
    mouth_shape = MouthShape()
    for key, val in [ (x, shape[x]) for x in [61,146,91,181,84,17,314,405,321,375,291] ]:
        mouth_shape.outer_bottom[key] = val
    for key, val in [ (x, shape[x]) for x in [61,185,40,39,37,0,267,269,270,409,291] ]:
        mouth_shape.outer_top[key] = val
    for key, val in [ (x, shape[x]) for x in [78,95,88,178,87,14,317,402,318,324,308] ]:
        mouth_shape.inner_bottom[key] = val
    for key, val in [ (x, shape[x]) for x in [78,191,80,81,82,13,312,311,310,415,308] ]:
        mouth_shape.inner_top[key] = val
    return mouth_shape

def print_mouth_points(frame,shape):
    mouth_shape = get_mouth_points(shape)
    for (x,y) in mouth_shape.outer_bottom.values():
        cv2.circle(frame, (x,y), 2, (0, 0, 255), -1)
    for (x,y) in mouth_shape.outer_top.values():
        cv2.circle(frame, (x,y), 2, (0, 0, 255), -1)
    for (x,y) in mouth_shape.inner_bottom.values():
        cv2.circle(frame, (x,y), 2, (0, 0, 255), -1)
    for (x,y) in mouth_shape.inner_top.values():
        cv2.circle(frame, (x,y), 2, (0, 0, 255), -1)
    return frame

class Iris:
    def __init__(self):
        self.left = {}
        self.right = {}
        
def get_iris_points(shape):
    iris_shape = Iris()
    for key, val in [ (x, shape[x]) for x in [473,474,475,476,477] ]:
        iris_shape.left[key] = val
    for key, val in [ (x, shape[x]) for x in [468,469,470,471,472] ]:
        iris_shape.right[key] = val
    return iris_shape

def print_iris_points(frame,shape):
    iris_shape = get_iris_points(shape)
    for (x,y) in iris_shape.left.values():
        cv2.circle(frame, (x,y), 2, (0,128,255), -1)
    for (x,y) in iris_shape.right.values():
        cv2.circle(frame, (x,y), 2, (0,128,255), -1)
    return frame



def get_head_points(shape):
    head_points = {  "nosetip" : {},
                 "chin" : {},
                 "lefteyecorner" : {},
                 "righteyecorner" : {},
                 "leftmouthcorner" : {},
                 "rightmouthcorner" : {}
                  }
    head_points["nosetip"][4] = shape[4]
    head_points["chin"][175] = shape[175]
    head_points["lefteyecorner"][33] = shape[33]
    head_points["righteyecorner"][263] = shape[263]
    head_points["leftmouthcorner"][61] = shape[61]
    head_points["rightmouthcorner"][291] = shape[291]
    return head_points

def print_head_points(frame, shape):
    head_points = get_head_points(shape)
    for dictt in head_points.values():
        for val in dictt.values():
            cv2.circle(frame, val, 2, (255,0,0), -1)
    return frame