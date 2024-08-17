import cv2

img = cv2.imread('data/cat.jpg') # 이미지 부르기(NumPy 배열로 반환)

cv2.namedWindow('Display Window') # display window 만들기

cv2.imshow('Display Window', img) # display window에 이미지 올리기
cv2.imwrite('data/copy.jpg', img) # 이미지 저장하기

cv2.waitKey() # 키 입력 대기

cv2.destroyAllWindows() # 키 입력되면 window 다 삭제
