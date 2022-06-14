'''
객체 => cv2.cvtColor( src, code, dst+None, dstCn=None)
                    src: 입력영상  / dst: 출력영상  / dstCn: 채널수 (0이면 자동처리)
                    code: cv2.COLOR_BGR2GRAY  <=> cv2.COLOR_GRAY2BGR
                        :           BGR2RGB   <=>            RGB2BGR
                        :           BGR2HSV   <=>
                        :           BGR2YCrCb <=>
히스토그램(Histogram) >> 분포도
- 영상의 픽셀값 분포를 그래프의 형태로 표현한 것.
- GRAYSCALE 영상에서 각 GRAYSCALE값에 해당하는 픽셀의 갯수를 구하고
  막대그래프의 형태로 표현가능

정규화된 히스토그램(Normalization Histogram)
- 각 픽셀의 갯수를 영상 전체 픽셀의 갯수로 나눠 준 것.
- 해당 그레이스케일 값을 갖는 픽셀이 나타날 확률을 잡는 것.

 히스토그램 구하기
cv2.calcHist(images, channels, msk, histSize, ranges, hist=None, accmulate=None)
#               images : 입력 영상 리스트
#               channels : 히스토그램을 구할 채널을 나타내는 리스트
#               msk : 마스크 영상, 입력 영상 전체에서 히스토그램을 구하려면 None으로 지정함.
#               histSize : 히스토그램 각 차원의 크기를 나타내는 리스트
#               ranges : 히스토그램 각 차원의 최소값과 최대값으로 구성된 리스트
#               hist : 계산된 히스토그램(numpy.ndarray)
#               accmulate : 기존의 hist 히스토그램에 누적하려면 True, 새로 만들려면 False
'''
import sys
import cv2
import matplotlib.pyplot as plt

# 색상, 농도분포도 구하기
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print("영상 ㄴㄴ")
    sys.exit()
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('SRC', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()

cv2.destroyAllWindows()