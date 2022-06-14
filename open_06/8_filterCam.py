'''
- 필터 카메라 프로그램을 제작하자.

   - 캠을 이용해서 아래 기능을 구현해 보자.
   - blur
   - edge
   - spacebar를 누를 때마다 모드가 변경하는 캠 필터 프로그램을 작성해 보자.

   - 양방향 필터링 함수
     - bilateralFilter()
     - 양방향 필터
        - 에지 보전 잡음 제거 필터
        - 평균값 필터 또는 가우시안 필터는 에지 부근에서도 픽셀값을 평탄하게 만드는 단점(또는 특징)이 있음.
        - 기준 픽셀과 이웃 픽셀과의 거리, 픽셀값의 차이를 함께 고려하여 블러링 정도를 조절함.
        - 이미지 끝 부분, 모서리, 산 꼭대기를 특징적인 것은 살리고, 나무가지 , 각을 나타내는 이미지 등등 살림.
          기타 부수적인 것은 블러링 처리함. (엣지가 아닌 부분만 블러링 처리함.)

        - cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, dst=None, borderType=None)
          src : 입력 영상
          d : 필터링에 사용될 이웃 픽셀의 거리(지름), -1을 입력하면 sigmaSpace값에 의해 자동 결정됨.
               -1을 많이 사용함.
          sigmaColor: 색 공간에서 필터의 표준 편차 입력
          sigmaSpace: 좌표 공간에서 필터의 표준 편차 입력

        - cv2.Canny()
          - 엣지 검출 함수
          - 이미지의 엣지만을 리턴함.

          - cv2.Canny(minVal, maxVal)
            - minVal : 최소 임계값
            - maxVal : 최대 임계값
            - 임계값이 클수록 엣지가 검출되기 어렵고, 작을수록 엣지가 검출되기 쉬움.
            - 머리카락 크기도 찾아냄.
'''
import  sys
import  numpy  as np
import  cv2

def  cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))   # frame을 줄여주는 작업
    blr  = cv2.bilateralFilter(img2, -1, 20, 7)   # 20 블러링, 7 : sigmaSpace로 블러링하겠음.
    edge = 255 - cv2.Canny(img2, 80, 120)  # 영상의 라인 쪽을 반전시킴.
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    dst  =  cv2.bitwise_and(blr, edge)              # blr & edge
    dst  =  cv2.resize(dst, (w, h), interpolation=cv2.INTER_LINEAR)
    # 보관법으로 픽셀이 깨지거나, 뿌엿게 되는 것을 방지함.(INTER_NEAREST 등 있음.)
    return  dst

def  sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr  = cv2.GaussianBlur(gray, (0,0), 3)
    dst  = cv2.divide(gray, blr, scale=255)   # 흑백영상을 블러로 나눈 값을 255로 곱함.
    return dst

cap = cv2.VideoCapture(0)
cam_mode = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:            # 27 : 아스키코드 = ESC
        break
    elif key == ord(' '):    # ord() <-- 아스크 코드를 읽어라. spacebar를 누르면
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0

cap.release()                # cap객체를 해제함.
cv2.destroyAllWindows()













