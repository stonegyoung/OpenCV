import cv2
import numpy as np

# 화이트 캔버스 만들기
canvas = np.full((640, 640,3), 255, dtype='uint8')

# 좌표는 # 0~639까지
# (x, y) 
# x: 가로
# y: 세로

# 검은색 직선
cv2.line(canvas, (0,0), (639,639), (0,0,0), 3) # 이미지, 시작 좌표, 끝 좌표, rgb, 선 두께, 선 종류

# 빨간색 사각형
cv2.rectangle(canvas, (200,200), (439, 439), (0,0,255), 5) # 이미지, 시작 좌표, 끝 좌표, bgr, 선 두께, 선 종류

# 초록색 사각형
cv2.rectangle(canvas, (10,10,100,20), (0,255,0)) # 이미지, (x,y,w,h), bgr, 선 두께, 선 종류

# 파란색 원
cv2.circle(canvas, (250,250), 50, (255,0,0), 2) # 이미지, 중심 좌표, 반지름,  bgr, 선 두께, 선 종류

# 보라색 다각형
pts = np.array([[10,10], [300,400], [70,40], [50,500]])
cv2.polylines(canvas, [pts], True, (128,0,128), 2) # 이미지, 좌표들, 처음과 끝 좌표 잇는지, bgr, 선 두께, 선 종류

# 검정색 글씨
cv2.putText(canvas, 'drawing', (300,300), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,0)) # 이미지, 텍스트, 텍스트의 왼쪽 아래 좌표, 폰트 종류, 폰트 크기 비율, bgr , 선 두께, 선 종류

cv2.imshow('draw', canvas)

cv2.waitKey()
cv2.destroyAllWindows()