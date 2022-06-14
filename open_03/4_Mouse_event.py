'''
------------------- [마우스 이벤트] ---------------------
                                              생략가능
cv2.setMouseCallback( windowName, onMouse,  param=None )   <= 설정
        이벤트 처리할    창의 이름    콜백함수     콜백함수에
                                   이름       전달할 데이터

                  *onMouse( event,  x, y,     flags,      param )  <= 실행
                마우스이벤트의: 종류   실행좌표   이벤트발생시   setMouseCallback
                                               상태        에서 설정한 데이터
'''
# 그림판 만들기

import cv2
import numpy as np

oldx = oldy = -1

def on_mouse(event, x,y, flags, param):
    global oldx, oldy #밖에서 선언한거 쓸수있음 (전역변수 사용가능)
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x,y
        print("왼쪽 버튼 클릭: %d, %d" %(x,y))

    elif event == cv2.EVENT_LBUTTONUP:
        print("왼쪽 버튼 뗌: %d, %d" %(x,y))

    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:        # 핑크    굵기    선모양
            cv2.line(img, (oldx, oldy), (x,y), (255,51,255), 4, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y
img = np.ones((480,640,3), dtype = np.uint8) *255
cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)

cv2.imshow('Image', img)
cv2.waitKey()
cv2.destroyAllWindows()

