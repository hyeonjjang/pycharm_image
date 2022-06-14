'''
필터링
영상의 필터링
영상에서 필요한 정보만 통과시키고 원치 않는 정보는 걸러내는 작업

공간적 필터링
* 영상의 픽셀값을 직접 이용하는 필터링 방법
* 대상 좌표의 픽셀값과 주변 픽셀값을 동시에 사용
* 마스크 연산을 이용
(마스크 = 커널(kernel) = 윈도우(window) = 템플릿(template))

* 마스크의 형태와 값에 따라 필터의 역할이 결정됨
    1. 영상 부드럽게 만들기
    2. 영상 날카롭게 만들기
    3. 엣지 검출
    4. 잡음 제거

OpenCV 필터링에서 지원하는 가장자리 픽셀 확장

BORDER_CONSTANT : 000abcdefgh000
BORDER_REPLICATE : aaaabcdefghhhh
BORDER_REFLECT_101 : dcbabcdefghgfe (디폴트)

cv2.filter2D(src, ddepth, kernel, dst=None, anchor=None, delta=None, borderType=None)
src : 입력 영상
ddepth : 출력 영상 데이터 타입 예) cv2.CV_8U, cv2.CV_23F, -1을 지정하면 src 동일한 타입
kernel : 필터 마스크 행렬
anchor : 고정점 위치, (-1,-1)이면 자동으로 필터 중앙을 고정점으로 사용
delta : 추가적으로 더할 값
borderType : 가장자리 픽셀 확장 방식
dst : 출력 영상

평균값 필터(Mean filter)
- 영상의 특정 좌표값을 주변 픽셀값들의 산술 평균으로 설정
- 픽셀들 간의 그레이스케일 값 변화가 줄어들어 날카로운 엣지가 무뎌지고 영상에 있는 잡음의 영향이 사라지는 효과

* 마스크 크기가 커질수록 평균값 필터 결과가 부드러워짐(많은 연산량이 필요)

cv2.blur(src, ksize, dst=None, anchor=None, borderType=None)
ksize : 평균값 필터 크기. (width, height) 형태의 튜플

'''
import  sys
import  cv2
import  numpy as np

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('영상을 읽을 수 없습니다.')
    sys.exit()
# 1 ========================================
'''
kernel = np.array([ [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9] ])
dst = cv2.filter2D(src, -1, kernel)
'''
# 2 ========================================
'''
kernel = np.ones((3, 3), dtype=np.float64)  /  9
dst = cv2.filter2D(src, -1, kernel)
'''
# 3 ========================================
dst = cv2.blur(src, (3, 3))
# 3 ========================================

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()













