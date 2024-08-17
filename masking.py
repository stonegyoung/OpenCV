import cv2


# 셋 다 사이즈가 똑같아야 함
src = cv2.imread('data/cat.jpg') # 원본 이미지
mask = cv2.imread('data/cat_mask.jpg') # 마스크 이미지
dst = cv2.imread('data/cat_redcarpet.jpg') # 검은 색 부분에 들어갈 값

# 이미지 복사. 원본을 마스킹해서 새로운 곳에 갖다 붙여라
mask_img = cv2.copyTo(src, mask, dst)

cv2.imshow('masking', mask_img)

cv2.waitKey()
cv2.destroyAllWindows()