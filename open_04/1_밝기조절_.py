'''
------------ [ 영상의 화소 처리 ] --------------
화소처리 : 입력 영상의 특정 좌표 픽셀값을 변경하여
         => 출력 영상의 해당 좌표 픽셀값으로 설정하는 연산 (0~255)

밝기조절 :  cv2.add(src1, src2, dst=None, mask=None, dtype=None)
           cv2.subtract ( src1, src2,  dst=None, mask=None,  dtype=None)
                         1영상   2영상   1+2영상    마스크영상    출력영상타입
                         --  크기 다 같아야함 --     0 or 1
----------------------------------------------'''
import sys
import cv2

# 흑백영상 밝기 조절
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("영상 불러올수 없다")
    sys.exit()
dst = cv2.add(src, 100) # 100더한 화소

cv2.imshow('src', src)  # 원본 흑백
cv2.imshow('dst', dst)  # 100더한 화소
cv2.waitKey()
cv2.destroyAllWindows()

# 컬러영상 밝기 조절
src2 = cv2.imread('cat.bmp')
if src2 is None:
    print("영상 ㄴㄴ")
    sys.exit()
dst2 = cv2.add(src2, (100,100,100,0))

cv2.imshow('src2', src2)
cv2.imshow('dst2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()

