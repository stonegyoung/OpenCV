# https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_detection.md
import mediapipe as mp
import cv2

mp_facedetection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_facedetection.FaceDetection()


img = cv2.imread('data/karina.jpg')
    
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
# 결과
result = face_detection.process(img_rgb) # rgb로 넣어줘야 한다
    
# print(result.detections)

img_height, img_width, _ = img.shape
    
# 얼굴 인식이 됐다면
if result.detections:
    for detection in result.detections:
        mp_drawing.draw_detection(img, detection)
        # 두 방식이 같다
        print(detection.location_data.relative_keypoints[mp_facedetection.FaceKeyPoint.NOSE_TIP]) 
        print(mp_facedetection.get_key_point(
          detection, mp_facedetection.FaceKeyPoint.NOSE_TIP))
        
        nose = detection.location_data.relative_keypoints[mp_facedetection.FaceKeyPoint.NOSE_TIP]
        # 실제 좌표
        nose_x = int(nose.x * img_width)
        nose_y = int(nose.y * img_height)
        
        cv2.putText(img, 'nose', (nose_x, nose_y), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,0), 2)
        
        # print(dir(mp_facedetection.FaceKeyPoint))
cv2.imshow('face_detection', img)
    
cv2.waitKey() 
cv2.destroyAllWindows()
    