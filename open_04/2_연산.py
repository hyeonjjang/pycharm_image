'''
 -------------  [ 차이연산 Difficult] -----------------
 - 두 영상의 같은 위치에 존재하는 픽셀값에 대하여 뺄셈 연산을 수행한 후
   그 절대값을 결과 영사의 픽셀값으로 설정함.
 - cv2.absdiff( src1, src2, dst=None)
                영상1   2     차이연산
                            결과 영상
-----------------------------------------------------'''
import sys
import cv2
from matplotlib import pyplot as plt

src1 = cv2.imread('lena.bmp', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)
if src1 is None or src2 is None:
    print("영상 ㄴㄴ")
    sys.exit()

dst1 = cv2.add(src1, src2, dtype=cv2.CV_8U) #합성
dst2 = cv2.subtract(src1, src2) # 자르기
dst3 = cv2.absdiff(src1, src2) # 반전

plt.subplot(221), plt.axis('off'), plt.imshow(src1,'gray'), plt.title('src1') # 원본
plt.subplot(222), plt.axis('off'), plt.imshow(dst1,'gray'), plt.title('add') # 합성
plt.subplot(223), plt.axis('off'), plt.imshow(dst2,'gray'), plt.title('substract') # 자르기
plt.subplot(224), plt.axis('off'), plt.imshow(dst3,'gray'), plt.title('absdiff') # 반전

plt.show()

''' ------- 영상에 대한 비트연산  ---------
cv2.bitwise_and(src1, src2, dst=None, mask=None) --> &
cv2.bitwise_or(src1, src2, dst=None, mask=None)  --> |
cv2.bitwise_xor(src1, src2, dst=None, mask=None) --> ^
cv2.bitwise_and(src1,       dst=None, mask=None) --> ~
# 각각의 픽셀값을 이진수로 표현하고 비트단위 논리연산을 수행함.
'''