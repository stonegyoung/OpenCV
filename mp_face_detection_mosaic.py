'''
사진에서 얼굴 검출
-> 바운딩박스 잘라
-> 축소
-> 확대
축소 확대하면 이미지 픽셀이 깨진다
-> 그걸 다시 원본 자리에
'''

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
    
print(result.detections)
    
# 얼굴 인식이 됐다면
if result.detections:
    for detection in result.detections:        
        # 실제 이미지 height, width
        img_height, img_width, _ = img.shape
        
        # bbox값 가져오기
        bbox = detection.location_data.relative_bounding_box # xmin: 0.362439603 ymin: 0.277495772 width: 0.291663319 height: 0.233330518
        
        # 실제 좌표와 크기 구하기
        xmin = int(bbox.xmin * img_width)
        ymin = int(bbox.ymin * img_height)
        width = int(bbox.width * img_width)
        height = int(bbox.height * img_height)
        
        # bbox(얼굴) 만큼 가져오기
        face = img[ymin:ymin+height, xmin:xmin+width]
        
        # 이미지 축소
        face = cv2.resize(face, (10,10))
        # 이미지 확대
        face = cv2.resize(face, (width, height))
        
        # 붙이기
        img[ymin:ymin+height, xmin:xmin+width] = face
        
cv2.imshow('mosaic', face)
cv2.imshow('face_detection', img)
    
cv2.waitKey() 
cv2.destroyAllWindows()
    