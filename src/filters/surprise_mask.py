import cv2
import itertools
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt

from PIL import Image

class gl():
    right_eye_x = 0
    right_eye_y = 0
    left_eye_x = 0
    left_eye_y = 0
    nose_x = 0
    nose_y = 0
    mouth_x = 0
    mouth_y = 0
    right_ear_x = 0
    right_ear_y = 0
    left_ear_x = 0
    left_ear_y = 0


def face_recognition(face_detection_results, mp_face_detection):
    print("FACE REGOGNITION FUNCTION§")
    if face_detection_results.detections:
        for face_no, face in enumerate(face_detection_results.detections):
            print(f'FACE NUMBER: {face_no+1}')
            print('---------------------------------')
            print(f'FACE CONFIDENCE: {round(face.score[0], 2)}')
            face_data = face.location_data
            print(f'\nFACE BOUNDING BOX:\n{face_data.relative_bounding_box}')

            print(f'{mp_face_detection.FaceKeyPoint(0).name}:')
            my_list = str(face_data.relative_keypoints[0])
            my_list = my_list.split()
            gl.right_eye_x = my_list[1]
            gl.right_eye_y = my_list[3]

            print(f'{mp_face_detection.FaceKeyPoint(1).name}:')
            my_list = str(face_data.relative_keypoints[1])
            my_list = my_list.split()
            gl.left_eye_x = my_list[1]
            gl.left_eye_y = my_list[3]

            print(f'{mp_face_detection.FaceKeyPoint(2).name}:')
            my_list = str(face_data.relative_keypoints[2])
            my_list = my_list.split()
            gl.nose_x = my_list[1]
            gl.nose_y = my_list[3]

            print(f'{mp_face_detection.FaceKeyPoint(3).name}:')
            my_list = str(face_data.relative_keypoints[3])
            my_list = my_list.split()
            gl.mouth_x = my_list[1]
            gl.mouth_y = my_list[3]

            print(f'{mp_face_detection.FaceKeyPoint(4).name}:')
            my_list = str(face_data.relative_keypoints[4])
            my_list = my_list.split()
            gl.right_ear_x = my_list[1]
            gl.right_ear_y = my_list[3]

            print(f'{mp_face_detection.FaceKeyPoint(5).name}:')
            my_list = str(face_data.relative_keypoints[5])
            my_list = my_list.split()
            gl.left_ear_x = my_list[1]
            gl.left_ear_y = my_list[3]


def get_locations_by_pixels(h, w):
    gl.left_eye_x = round(float(gl.left_eye_x) * w)
    gl.left_eye_y = round(float(gl.left_eye_y) * h)
    gl.right_eye_x = round(float(gl.right_eye_x) * w)
    gl.right_eye_y = round(float(gl.right_eye_y) * h)
    gl.nose_x = round(float(gl.nose_x) * w)
    gl.nose_y = round(float(gl.nose_y) * h)
    gl.mouth_x = round(float(gl.mouth_x) * w)
    gl.mouth_y = round(float(gl.mouth_y) * h)
    gl.right_ear_x = round(float(gl.right_ear_x) * w)
    gl.right_ear_y = round(float(gl.right_ear_y) * h)
    gl.left_ear_x = round(float(gl.left_ear_x) * w)
    gl.left_ear_y = round(float(gl.left_ear_y) * h)


def image_overlay_with_transparence(img1, img2, location):
    h,w,_ = img2.shape
    x,y = location
    shapes = np.zeros_like(img1, np.uint8)
    shapes[y:y+h, x:x+w] = img2
    alpha = 0
    mask = shapes.astype(bool)
    img1[mask] = cv2.addWeighted(img1, alpha, shapes, 1-alpha, None)[mask]
    return img1

def image_overlay_second(img1, img2, location):
    h, w = img2.shape[:2]
    h1, w1 = img2.shape[:2]
    x, y = location
    roi = img1[y:y + h1, x:x + w1]

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    img_bg = cv2.bitwise_and(roi, roi, mask=mask)
    img_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)
    dst = cv2.add(img_bg, img_fg)
    img1[y:y + h1, x:x + w1] = dst
    return img1


def display_eyes(img_copy, left_eye, right_eye):
    print("Result= ", gl.left_eye_x - gl.right_eye_x)
    size_eye = round(0.80 * (gl.left_eye_x - gl.right_eye_x))
    print("Size eye= ", size_eye)
    print('Original Dimensions : ',left_eye.shape)
    width = size_eye
    height = size_eye
    dim = (width, height)
    # resize image of eye
    resized_left = cv2.resize(left_eye, dim, interpolation = cv2.INTER_AREA)
    resized_right = cv2.resize(right_eye, dim, interpolation = cv2.INTER_AREA)
    print('Resized Dimensions : ',resized_left.shape)

    after_overlay = image_overlay_second(img_copy, resized_left, location=(gl.left_eye_x - round(size_eye/2), gl.left_eye_y - round(size_eye/2)))
    after_overlay = image_overlay_second(after_overlay, resized_right, location=(gl.right_eye_x - round(size_eye/2), gl.right_eye_y - round(size_eye/2)))
    return after_overlay


def surprise_face(path):
    sample_img = cv2.imread(path)
    img_copy = sample_img.copy()
    h,w,_ = img_copy.shape

    left_eye = cv2.imread('images/s_right.jpg')
    right_eye = cv2.imread('images/s_left.jpg')

    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5)
    mp_drawing = mp.solutions.drawing_utils
    face_detection_results = face_detection.process(img_copy)


    face_recognition(face_detection_results, mp_face_detection)
    get_locations_by_pixels(h, w)
    after_overlay = display_eyes(img_copy, left_eye, right_eye)

    # CONVERT IMAGE TO PILLOW IMAGE
    img = cv2.cvtColor(after_overlay, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
    return im_pil