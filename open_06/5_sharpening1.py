'''
언샤프 마스크 필터(Unsharp mask)
- 날카롭지 않은 영상 또는 부드러워진 영상을 이용하여 -> 날카로운 영상으로 생성.

clip()
- 배열에서 값을 하한 ~ 상한 값의 범위로 값을 자르는 함수
- np.clip(array, 하한값, 상한값)
  -----------------------------(예제)
  arr = np.arange(10)
  #array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  np.clip(arr, 2, 7)
  #array(2, 2, 2, 3, 4, 5, 6, 7, 7, 7)  <-- 결과값
  -----------------------------(예제)
  arr = np.array([ [4, 5, 2],
                   [1, 9, 3],
                   [7, 6, 8] ])
  np.clip(arr, 2, 7)
     
          # np.array([ [4, 5, 2],
                       [2, 7, 3],
                       [7, 6, 7] ])     <-- 결과값
'''
import  cv2
import  numpy as np

src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
blr = cv2.GaussianBlur(src, (0,0), 2)
dst = np.clip(2.0 * src - blr, 0, 255).astype(np.uint8)

# 날카로워짐 --> 각이 만들어져 있어서 그렇다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()