'''
 * 영상 확대 축소
크기변환(Scale transformation)
- 영상의 크기를 원본 영상보다 크게 또는 작게 만드는 변환
- x축과 y축 방향으로의 스케일 비율을 지정

    cv2.resize(src, dsize, dst=None, fx=None, fy=None, interpolation=None)
    dsize : 결과 영상 크기. (w, h) 튜플. (0, 0)이면 fx와 fy값을 이용하여 결정
    fx, fy : x와 y방향 스케일 비율. dsize 값이 0일 때만 유효
    interpolation : 보간법 지정
        cv2.INTER_NEARSET : 최근방 이웃 보간법
        cv2.INTER_LINEAR : 양선형 보간법(2x2 이웃 픽셀 참조)
        cv2.INTER_CUBIC : 3차회선 보간법(4x4 이웃 픽셀을 참조)
        cv2.INTER_LANCZOS4 : Lanczos 보간법(8x8 이웃 픽셀을 참조)
        cv2.INTER_AREA : 영상 축소시 효과적

  * 영상 축소시 고려할 사항
- 영상 축소시 디테일이 사라지는 경우가 발생(한 픽셀로 구성된 부분)
- 입력 영상을 부드럽게 필터링한 후 축소, 다단계 축소
- OpenCV의 cv2.resize() 함수에서 cv2.INTER_AREA 플래그를 사용
'''
import cv2

src = cv2.imread('cat.bmp')  # src.shape = (640, 480)

dst1 = cv2.resize(src, (0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst2 = cv2.resize(src, (2560, 1920))   # interpolation=cv2.INTER_LINEAR 기본값
dst3 = cv2.resize(src, (2560, 1920), interpolation=cv2.INTER_CUBIC)
dst4 = cv2.resize(src, (2560, 1920), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow('dst1', dst1[500:1600, 1000:1800])  # src.shape = (2560, 1920) 기본값
cv2.imshow('dst2', dst2[500:1600, 1000:1800])
cv2.imshow('dst3', dst3[500:1600, 1000:1800])
cv2.imshow('dst4', dst4[500:1600, 1000:1800])  # 1>2>3>4 점점 선명해짐
cv2.imshow('src', src)

cv2.waitKey()
cv2.destroyAllWindows()