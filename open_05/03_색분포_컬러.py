import sys
import cv2
import matplotlib.pyplot as plt

src = cv2.imread('cat.bmp')
if src is None:
    print("영상 ㄴㄴ")
    sys.exit()

colors = ['b', 'g', 'r']
bgr_plane = cv2.split(src)
print(bgr_plane)

for (p, c) in zip(bgr_plane, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)

cv2.imshow('SRC', src)
cv2.waitKey(1)
plt.plot(hist)
plt.show()

cv2.destroyAllWindows()