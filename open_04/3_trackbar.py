''' -------  [트랙바(trackbar) 만들기] ------
프로그램 동작중 사용자가 지정한 범위 안의 값을 선택 할 수 있는 컨트롤
OpenCv에서 제공하는 그래픽 사용자 인터페이스
cv2.createTrackbar(trackbarName, windowName,  value,      count,  onChange)
             트랙바:   이름          창이름     위치초기값   최대값(15)   콜백함수
                                                         최소(0)    def onChange(pas):
---------------------------------------------'''
#                     밝기조절
# 트랙바 이용하여 grayscale level 표현 (영상크기: 480,640   트랙바단계: 16 level)
import cv2
import numpy as np
def on_change(pos):
    print(pos)
    value = pos * 16
    if value >= 255:
        value = 255
    img[:] = value
    cv2.imshow('img', img)

img = np.zeros( (480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level','image', 0, 16, on_change) # 16레벨로 밝기조절 가능

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()