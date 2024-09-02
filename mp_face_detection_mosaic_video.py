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
    
    # 값이 계산되는 동안에 얼굴을 틀어서 이미지 좌표가 바뀌지 않게 lock
    frame.flags.writeable = False
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 얼굴 인식 결과
    result = face_detection.process(frame_rgb) # rgb로 넣어줘야 한다
    # print(result.detections)
    
    frame.flags.writeable = True
    
    # 실제 프레임 height, width
    img_height, img_width, _ = frame.shape
    
    # 얼굴 인식이 됐다면
    if result.detections:
        for detection in result.detections:
            # bbox값 가져오기
            bbox = detection.location_data.relative_bounding_box
            
            # 실제 좌표와 크기 구하기
            xmin = int(bbox.xmin * img_width)
            ymin = int(bbox.ymin * img_height)
            face_width = int(bbox.width * img_width)
            face_height = int(bbox.height * img_height)
            
            # bbox(얼굴) 만큼 가져오기
            
            face = frame[ymin:ymin+face_height, xmin:xmin+face_width]
             # 이미지 축소
            face = cv2.resize(face, (10,10))
            # 이미지 확대
            face = cv2.resize(face, (face_width, face_height))
            
            # 붙이기
            frame[ymin:ymin+face_height, xmin:xmin+face_width] = face
        
    cv2.imshow('face_detection', frame)
    
    if cv2.waitKey(1) == 27:
        break 
    
cap.release()
cv2.destroyAllWindows()
    