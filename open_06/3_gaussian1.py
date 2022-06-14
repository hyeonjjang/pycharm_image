'''
가우시안 필터(Gaussian filter)

- 평균값 필터에 의한 블러링의 단점을 극복한 것.
- 가까운 픽셀은 큰 가중치를, 멀리 있는 픽셀은 작은 가중치를 사용하여 계산함.
- 가우시안 함수 (인터넷으로 확인하자)
   평균과 표준편차에 의해 (값)그래프가 달라짐.
   뮤, 시스마
   ※ ( 정규 분포, 표준 정규 분포)
cv2. GaussianBlur(src, ksize, sigmaX, dst=None, sigmaY=None, borderType=None)
src : 입력 영상
ksize : 가우시안 커널(마스크) 크기, (0, 0)을 지정하면 -> sigma값에 의해 자동 결정됨.
sigmaX : x방향 sigma
sigmaY : y방향 sigma, 0이면 -> sigmaX와 같게 설정함.
borderType : 가장자리 픽셀 확장 방식

(x축이 -> sigma인데 -> 값을 늘리면 : 그래프 선이 완만해지고, 줄이면 그래프 선이 예리해짐.)
'''
import  cv2

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.GaussianBlur(src, (0, 0), 3)
dst2 = cv2.blur(src, (7, 7))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
