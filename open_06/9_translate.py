'''
- 기하학적 변환

   - 영상을 구성하는 픽셀의 배치 구조를 변경함으로 전체 영상의 모양을 바꾸는 작업.

      영상을 이동시키거나, 기울이거나, 3D적으로 틀어준다거나 하는 작업

      은행권에서 신분증을 사진으로 찍을 때 -> 바르게 찍어지지 않음 -> 고로 기하학적 변환으로
      바르게 영상을 잡아주는 기술임.

 - 이동 변환(Translation Transformation)

      - 가로 또는 세로 방향으로 영상을 특정 크기만큼 이동시키는 작업
      - x축과 y축 방향으로의 이동 변위를 지정함. (좌표가 바뀜)

     - warpAffine(src, M, dsize, dst=None, flags=None, borderMode=None, borderValue=None)
        - src : 입력영상
        - M : 2x3어파인(공간) 변환 행렬, 실수형
        - dsize : 결과 영상 크기.   (w, h)튜플, (0, 0)이면 src와 같은 크기로 설정하겠다.
        - flags : 보간법. 기본값은 cv2.INTER_LINEAR
        - borderMode : 가장자리 픽셀 확장 방식, 기본값은 cv2.BORDER_CONSTANT
        - borderValue : cv2.BORDER_CONSTANT일 때 사용할 상수 값, 기본값은 0임.

[ [1, 0, 200],
   [0, 1, 100] ]

x' = x + a
y' = y + b

|  1  0  | [ x ]   + | a |
|  0  1  | [ y ]      | b |  ---> 곱셈으로 바꿈.

                | x |  <--  2x3어파인(공간) 변환 행렬만듬. --> aff가 처리해줌.
| 1 0 a |  *  | y |
| 0 1 b |     | 1 |   ---> 200, 100을 이동시킨 것임.
                              (x만큼, y만큼)
'''

import sys
import cv2
import numpy as np

src = cv2.imread('cat.bmp')
aff = np.array([[1,0,200],
          [0,1,100]], dtype=np.float32)
dst = cv2.warpAffine(src, aff, (0,0))

cv2.imshow('src', src)
cv2.imshow('dst',dst)
cv2.waitKey()