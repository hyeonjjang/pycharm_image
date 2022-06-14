import matplotlib.pyplot as  plt
import cv2
# cv2        --> RGB가 아니라 --> BGR로 접근함.
# matplotlib --> RGB로 접근함.

imBGR = cv2.imread('cat.bmp')   # 컬러영상(Blue-> Green-> Read)
imRGB = cv2.cvtColor(imBGR, cv2.COLOR_BGR2RGB) # BGR -> RGB 변환함.
# 1차 실습 ----------------------------
# plt.axis('off')    # 격자 = grid 를 감춤.
# plt.imshow(imRGB)
# plt.show()

# 2차 실습 ----------------------------
imGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
# plt.axis('off')
# plt.imshow(imGray, cmap='gray')
# plt.show()

# 3차 실습 ----------------------------
plt.subplot(121)
plt.axis('off')      # 격자 = grid 를 감춤.
plt.imshow(imRGB)
plt.subplot(122)
plt.axis('off')
plt.imshow(imGray, cmap='gray')
plt.show()
