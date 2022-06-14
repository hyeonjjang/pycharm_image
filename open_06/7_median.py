'''
영상의 잡음(Noise)

- 영상의 픽셀 값에 추가되지 않은 원치 않은 형태의 신호(영상, 티.)

미디언 필터(Median filter)

- 주변 픽셀들의 값들을 정렬하여 그 중앙값(median)으로 픽셀값을 대체하는 것.
- '소금 -후추 잡음' 제거에 효과적임.

  48  60  72        48  60  72  52  102 88   69  84  92
  52  102 88  ->    48  52  60  69   72  84   88  92  102 (정렬함)
  69  84  92                        ---
                                   중앙값
-> 미디언 필터 결과
  48  52  60
  69  72  84
  88  92  102

- cv2.medianBlur(src, ksize, dst=None)
  ksize : 커널크기, 1보다 큰 홀수를 지정함.

- 잡음이 있는 파일 필요함.(noise.bmp)
'''
import  cv2
import  numpy  as np

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.medianBlur(src, 3)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
# 자연스럽지는 않음. 옛날 사진 복원하는 느낌. 많이 사용함.
cv2.destroyAllWindows()











