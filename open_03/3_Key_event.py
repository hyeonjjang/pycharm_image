'''
-----------  [키를 누르면 생기는 이벤트]  -------------
1. key event
    if  함수 이름 == ord('q'):
       (q 입력시 실행 문장)
---------------------------------------------------
'''
# 키를 누르면 사진의 반전효과 줌

import cv2
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백영상
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord('i') or keyvalue == ord('I'): # i/I 키 누르기
        img = ~img # 반전효과
        cv2.imshow('image', img)
    elif keyvalue == 27:
        break

cv2.destroyAllWindows()
