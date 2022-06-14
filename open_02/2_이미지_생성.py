# numpy.empty()   : 배열을 생성 --> 초기값들을 : 임의값 으로 채움.
# numpy.zeros()   : 배열을 생성 --> 초기값들을 : 0 으로 채움.
# numpy.ones()    : 배열을 생성 --> 초기값들을 : 1 으로 채움.
# numpy.full()    : 배열을 생성 --> 초기값들을 : 원하는값 으로 채움.
import  numpy  as np
import  cv2

img1 = np.empty( (240, 320), dtype=np.uint8 )
img2 = np.zeros( (240, 320, 3), dtype=np.uint8 )
img3 = np.ones( (240, 320), dtype=np.uint8 ) * 255
# [문제] --> 노란색으로 생성되게 만들어 보자. (R=255,G=255,B=0)
img4 = np.full((240,320,3),(0,255,255),dtype = np.uint8)
#                           B  G   R
# img4 = np.full((240,320,3),fill_value=(0,255,255),dtype = np.uint8)
cv2.imshow('name : img1', img1)
cv2.imshow('name : img2', img2)
cv2.imshow('name : img3', img3)
cv2.imshow('name : img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()