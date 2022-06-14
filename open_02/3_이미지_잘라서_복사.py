# -- 영상의 복사 --
# img2 = img1  : 객체가 기억하고 있는 주소를 복사한 것임. (똑같은 주소를 소유함.)
# img2 = img1.copy()
import cv2

img1 = cv2.imread('dog.jpg')
# http://maschek.hu/imagemap/imgmap/  <-- 부분영상을 추출하기위한 사이트
# 1. 파일선택 - 클릭 -> '강아지.jpg'파일 - 열기
# 2. upload버튼 - 클릭
# 3. accept 버튼 - 클릭
# 4. 강아지 앞면 얼굴을 드래그 -좌표값을 복사함.
# 5. 161,53,395,230
# 6.  x   y  w   h
img2 = img1[53: 300, 161: 500]          # 부분영상을 자른것임.
img3 = img1[53: 300, 161: 500].copy()

img2.fill(0)

cv2.imshow('name:img1', img1)
cv2.imshow('name:img2', img2)
cv2.imshow('name:img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()