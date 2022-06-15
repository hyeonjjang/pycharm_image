'''
cv2.rectangle(사각형을 넣을 이미지, 사각형 좌측상단 좌표,
              사각형 우측하단 좌표, 테두리선 색상, 테두리선 두께)
이미지 피라미드(Image pyramid)
* 하나의 영상에 대해 => 다양한 해상도의 영상 세트를 구성한 것
* 보통 가우시안 필터링 & 다운샘플링 형태로 축소하여 구성
    이미지를 작게 세트를 구성(다운 샘플링)
    이미지를 크게 세트를 구성(업 샘플링)

      cv2.pyrDown(src, dst=None, dstsize=None, borderType=None)
    dstsize : 출력 영상 크기. 따로 지정하지 않으면 입력 영상의 가로, 세로 크기의 1/2로 설정
        - 먼저 5x5 크기의 가우시안 필터를 적용
        - 짝수 행과 열을 제거하여 작은 크기의 영상을 생성

    cv2.pyrUp(src, dst=None, dstsize=None, borderType=None)
'''
import cv2

src = cv2.imread('cat.bmp')
rc = (250, 120, 200, 200)

cpy = src.copy()
cv2.rectangle(cpy, rc, (0,0,255),2)
cv2.imshow('src', cpy)
cv2.waitKey()

for i in range(1,4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0,0,255),2,shift=i)  # 배수만큼 줄어들게함
    cv2.imshow('src',cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')  # 원본만 닫기

cv2.destroyAllWindows()