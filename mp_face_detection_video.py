# https://github.com/google-ai-edge/mediapipe/blob/master/docs/solutions/face_detection.md
import mediapipe as mp
import cv2

mp_facedetection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

face_detection = mp_facedetection.FaceDetection()

# 웹캠
cap = cv2.VideoCapture(0)
    
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break    
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 얼굴 인식 결과
    result = face_detection.process(frame_rgb) # rgb로 넣어줘야 한다
    # print(result.detections)
    
    # 얼굴 인식이 됐다면
    if result.detections:
        for detection in result.detections:
            # 그려라
            mp_drawing.draw_detection(frame, detection) 
            
        
    cv2.imshow('face_detection', frame)
    
    if cv2.waitKey(1) == 27:
        break 
    
cap.release()
cv2.destroyAllWindows()
    