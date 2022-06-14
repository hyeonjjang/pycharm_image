import cv2
import sys
print('OpenCV 버전 : ', cv2.__version__)

img  =  cv2.imread('cat.bmp')

if img  is None:
    print("영상을 불러올 수 없습니다.!")
    sys.exit()    # 영상파일 불러오기 실패 - 에러 메시지 출력하고 종료시킴.

cv2.namedWindow('image') # 새창 이름이 'image' 임.
cv2.imshow('image', img) # image창에 img영상을 출력함.

cv2.waitKey()            # 키보드에 엔터키를 치면 -> 다름 프로그램으로 넘어감.
                         #  대기
cv2.destroyWindow()      # 모든창을 닫음