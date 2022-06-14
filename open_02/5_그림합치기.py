# https://www.iconfinder.com/
# PNG 파일은 => 알파채널 이므로, 따로 마스크 파일 안 만들어도 됨.
import sys
import cv2

src = cv2.imread("field.bmp", cv2.IMREAD_COLOR)
hero = cv2.imread('hero.png', cv2.IMREAD_UNCHANGED)

if src is None or hero is None:
    print("영상이 없다.")
    sys.exit()

mask = hero[ :, :, 3]    #  3 => B,G,R 3채널
hero = hero[ :, :, :-1]  # -1 => 알파채널
h, w = mask.shape[:2]   # 0(h:높이) ,1(w:가로)
crop = src[10:10+h, 10:10+w]  # batman, mask와 같은 크기 부분 추출

cv2.copyTo(hero, hero, crop)

cv2.imshow('window:src', src)
cv2.imshow('window:mask', mask)
cv2.imshow('window:hero', hero)

cv2.waitKey()
cv2.destroyAllWindows()