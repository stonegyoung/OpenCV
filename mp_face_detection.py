# https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_detection.md
import mediapipe as mp
import cv2

mp_facedetection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_facedetection.FaceDetection()


mp_img = cv2.imread('data/karina.jpg')
bbox_img = cv2.imread('data/karina.jpg')
    
img_rgb = cv2.cvtColor(mp_img, cv2.COLOR_BGR2RGB)
    
# 결과
result = face_detection.process(img_rgb) # rgb로 넣어줘야 한다
    
print(result.detections)
    
# 얼굴 인식이 됐다면
if result.detections:
    for detection in result.detections:
        # 그려라
        mp_drawing.draw_detection(mp_img, detection) 
        
        # bbox 알려줌: 좌표가 width와 height를 1로 봤을 때 얼만큼 위치했는지, 얼만큼 차지하는지(*width, *height하면 실제 좌표 나온다)        
        # print(detection.location_data.relative_bounding_box) 

        img_height, img_width, _ = mp_img.shape
        bbox = detection.location_data.relative_bounding_box # xmin: 0.362439603 ymin: 0.277495772 width: 0.291663319 height: 0.233330518
        xmin = int(bbox.xmin * img_width)
        ymin = int(bbox.ymin * img_height)
        width = int(bbox.width * img_width)
        height = int(bbox.height * img_height)
        cv2.rectangle(bbox_img, (xmin,ymin,width,height), (0,0,255), 3)
        
cv2.imshow('face_detection', mp_img)
cv2.imshow('bbox', bbox_img)
    
cv2.waitKey() 
cv2.destroyAllWindows()
    