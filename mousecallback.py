import numpy as np
import cv2

# 마우스 좌표 초기화
oldx = oldy = -1
bgr = (0,0,0)

# https://docs.opencv.org/3.4/d7/dfc/group__highgui.html#gab7aed186e151d5222ef97192912127a4
def on_mouse(event, x, y, flags, userdata):
    global oldx, oldy
    global bgr
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 좌클릭
        oldx, oldy = x, y
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 이동
        if flags & cv2.EVENT_FLAG_LBUTTON: # 마우스 좌클릭이 계속 되고 있으면 (flags는 아무 상태가 아니면 0)
            cv2.line(img, (oldx, oldy), (x,y), bgr, 2)
            cv2.imshow('Mouse Event', img)
            oldx, oldy = x, y
    if event == cv2.EVENT_RBUTTONDOWN: # 마우스 우클릭
        bgr = (np.random.randint(0,255), np.random.randint(0,255), np.random.randint(0,255)) # 색 바꾸기

img = np.full((640,640,3), 255, dtype=np.uint8)

cv2.imshow('Mouse Event', img)
# 마우스 클릭 이벤트
cv2.setMouseCallback('Mouse Event', on_mouse, img) # 창 이름, 콜백 함수명, 이미지
cv2.waitKey()
cv2.destroyAllWindows()
