'''
   투시 변환 행렬 구하기
    cv2.getPerspectiveTransform(src, dst)
    src : 4개의 원본 좌표점 numpy.ndarray.shape = (4, 2)
    dst : 4개의 결과 좌표점 numpy.ndarray.shape = (4, 2)

    영상의 투시 변환 함수
    cv2.warpPerspective(src, M, dsize, dst=None, flags=None, BorderMode=None, borderValue=None)
    M : 3x3 투시 변환 행렬. 실수형
    dsize : 결과 영상 크기. (w, h) 튜플. (0, 0)이면 src와 같은 크기로 설정

    투시 변환(Perspective Transform)
* 3x3 matrix

    p11 p12 p13
    p21 p22 p23
    p31 p32 1
'''
import cv2
src = cv2.imread('cat.bmp')

cp = (src.shape[1]/2, src.shape[0]/2)
rot = cv2.getRotationMatrix2D(cp,20,0.5)
dst = cv2.warpAffine(src, rot, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()