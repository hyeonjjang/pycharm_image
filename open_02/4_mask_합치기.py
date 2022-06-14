# 마스크 연산
# ROI
# -Region of Interest (관심 영역)
# - 영상 에서 특정 연산을 수행 하고자 하는 임의의 부분 연역을 말함

# OpenCV는 ROI연산을 지원
# 마스크 영상은 cv2.cv_8UC1(그레이스케일 영상) 타입임.
# 마스크 영상의 픽셀값이 0이 아닌 위치에서만 연산 수행
# 마스크 영상은 0 또는 255로 구성된 이진 영상

import sys
import cv2

src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane .bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print("영상을 불러 올수 없다.")
    sys.exit()

cv2.copyTo(src, mask, dst)
cv2.imshow('name:src', src)
cv2.imshow('name:mask', mask)
cv2.imshow('name:dst', dst)

# src (입력 영상) > mask > dst(출력 영상)

cv2.waitKey()
cv2.destroyAllWindows()