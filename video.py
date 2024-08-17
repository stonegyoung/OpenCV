import cv2

# mp4나 avi 혹은 웹캠
# cap = cv2.VideoCapture('./data/.mp4')
cap = cv2.VideoCapture(0) # 웹캠 사용해서 open

# 영상 저장을 위한
codec = cv2.VideoWriter_fourcc(*'DIVX')
fps = cap.get(cv2.CAP_PROP_FPS) # 비디오 프레임(fps) 받기
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(width, height)

out = cv2.VideoWriter('out.avi', codec, fps, (width, height)) # 동영상 저장할 변수

while True: # 영상이 계속 들어오면
    ret, frame = cap.read() # ret: frame이 잘 읽혔는지 T/F frame: 카메라에서 영상 읽어서 한 장 캡쳐
    
    ### 만약 모델을 만들었다면 이쪽에 넣어 ###
    if not ret: # 안읽히면
        break
    
    out.write(frame) # 영상 저장
    cv2.imshow('video', frame) # 실시간으로 영상 출력
    
    if cv2.waitKey(1) == 27: # ESC키면(아스키코드값으로 넣어준다)
        break
    
out.release()
cap.release()
cv2.destroyAllWindows()