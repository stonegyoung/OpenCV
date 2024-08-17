import cv2

src = cv2.imread('data/cat.jpg')

img = cv2.imread('data/redcarpet.jpg')
print(img.shape)

img = cv2.resize(img, (src.shape[1], src.shape[0])) # width, height 순으로
print(src.shape, img.shape) # 이미지 사이즈 체크

cv2.imwrite('data/cat_redcarpet.jpg', img) # resize된 이미지 저장
cv2.imshow('', img)
cv2.waitKey()
cv2.destroyAllWindows()