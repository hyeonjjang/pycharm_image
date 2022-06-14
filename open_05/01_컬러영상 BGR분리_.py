'''
1) opencv 컬러 영상
   => 3차원 numpy.ndarray(img.shape = (h, w, 3))
 img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) 흑백영상
 img2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR) 컬러영상
2) 채널 분리
   => cv2.split(m, mv=None)
               m: 다채널 영상(BGR) / mv: 출력영상 / dst: 출력의 영상리스트
2) 채널 결합
   => cv2.merge(mv, dst=None)
               mv: 입력 영상 리스트 / dst: 출력영상
'''
import cv2
import sys
src = cv2.imread('Candy.png', cv2.IMREAD_COLOR)
if src is None:
    print("영상 ㄴㄴ")
    sys.exit()
print("src의 shape: ", src.shape)   # (h,w,3개)
print("src의 type: ", src.dtype)    # unsigned int 8

b_plane, g_plane, r_plane = cv2.split(src)

# 2차원
print(b_plane); print("="*20)
print(g_plane); print("="*20)
print(r_plane)

cv2.imshow('SRC', src)   # B+G+R = SRC 컬러완성
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)

cv2.waitKey()
cv2.destroyAllWindows()

