# img1, img2 <--- numpy.ndarray
# numpy.ndarray --> ndim : 차원수
#               --> shape : (row, column), 각 차원의 크기, (h, w) or (h, w, 3)
#               --> size : 전체 원소 개수
#               --> dtype : 원소의 데이터 타입
import  cv2
img1 = cv2.imread('../open_01/cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('../open_01/cat.bmp', cv2.IMREAD_COLOR)
print('type(img1) : ', type(img1) )
print('type(img2) : ', type(img2) )
print('img1.shape : ', img1.shape)
print('img2.shape : ', img2.shape)
print('img1.dtype : ', img1.dtype)
print('img2.dtype : ', img2.dtype)

h, w = img2.shape[:2]   # h-> 480, w->640
print('image2 size : {} * {}'.format(h, w))

if len(img1.shape) == 2:
    print('img1은 흑백 영상입니다.')
elif len(img1.shape) == 3:
    print('img1은 컬러 영상입니다.')

if len(img2.shape) == 2:
    print('img2은 흑백 영상입니다.')
elif len(img2.shape) == 3:
    print('img2은 컬러 영상입니다.')

# 첫번쨰 실습
#for문으로 픽셀값을 변경하는 작업은 매우 느림.
#for y in range(h):
#    for x in range(w):
#        img1[y, x] = 255
#        img2[y, x] = (0, 0, 255)  # BGR
#cv2.imshow('img1', img1)
#cv2.imshow('img2', img2)
#cv2.waitKey()
#cv2.destroyAllWindows()

# 두번쨰 실습
#파이썬의 슬라이스 활용으로 픽셀값을 변경하는 작업을 매우 빠르게 처리함.
img1[ : , : ] = 255
img2[ : , : ] = (0, 0, 255)     # BGR

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()
cv2.destroyAllWindows()