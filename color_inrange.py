import cv2

img = cv2.imread('data/rgb.jpg')

red = cv2.inRange(img, (0,0,128), (128,128,255)) # 빨간 색만 뽑기
# cv2.imwrite('data/red.jpg', red)
blue = cv2.inRange(img, (128,0,0), (255,128,128)) # 파란 색만 뽑기
# cv2.imwrite('data/blue.jpg', blue)
green = cv2.inRange(img, (0,128,0), (128,255,128)) # 초록 색만 뽑기
# cv2.imwrite('data/green.jpg', green)

cv2.imshow('original', img)
cv2.imshow('red', red)
cv2.imshow('blue', blue)
cv2.imshow('green', green)

cv2.waitKey()
cv2.destroyAllWindows()