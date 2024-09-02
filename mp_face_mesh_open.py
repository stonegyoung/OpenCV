import cv2
from mediapipe.python.solutions import face_mesh as mp_face_mesh
import numpy as np


# print(dir(mp_face_mesh))
face_mesh = mp_face_mesh.FaceMesh()

def return_distance(v1, v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    
    return np.linalg.norm(v1-v2)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame.flags.writeable = False
    results = face_mesh.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    frame.flags.writeable = True
    
    img_height, img_width, _ = frame.shape

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # 실제 좌표 튜플로
            upper_lip = (int(face_landmarks.landmark[13].x * img_width), int(face_landmarks.landmark[13].y * img_height)) # 인덱스 13
            lower_lip = (int(face_landmarks.landmark[14].x * img_width), int(face_landmarks.landmark[14].y * img_height)) # 인덱스 14
            
            # 시각화
            cv2.circle(frame, upper_lip, 1, (0,0,255), 2)
            cv2.circle(frame, lower_lip, 1, (0,0,255), 2)
            
            # 거리 시각화
            # cv2.putText(frame, str(return_distance(upper_lip, lower_lip)), (0, 100), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0))
            
            distance = return_distance(upper_lip, lower_lip)
            if distance <= 5. : # close
                cv2.putText(frame, 'Close', (0,100), cv2.FACE_RECOGNIZER_SF_FR_COSINE, 3, (255,0,0))
            else:
                cv2.putText(frame, 'Open', (0,100), cv2.FACE_RECOGNIZER_SF_FR_COSINE, 3, (0,0,255))
     
            
            # print(face_landmarks.landmark[mp_face_mesh.FACEMESH_LIPS])

    cv2.imshow('', frame)
    if cv2.waitKey(1) ==27:
        break
cv2.destroyAllWindows()