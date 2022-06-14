import  cv2
import  numpy as np

src = cv2.imread('cat.bmp')

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) # 가우시안 접근시 가장 좋은 방법임.
src_f     = src_ycrcb[:, :, 0].astype(np.float32)
blr       = cv2.GaussianBlur(src_f, (0, 0), 2.0)
src_ycrcb[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)

dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)   # 훨씬 선명하게 보임.
cv2.waitKey()

cv2.destroyAllWindows()
