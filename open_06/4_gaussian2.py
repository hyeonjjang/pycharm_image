import  cv2
src = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
for sigma  in range(1, 6):
    dst = cv2.GaussianBlur(src, (0, 0), sigma)
    desc = 'Sigma = {}'.format(sigma)
    cv2.putText(dst, desc, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 0, 1, cv2.LINE_AA)
    cv2.imshow('dst', dst)
    cv2.waitKey()
    # 고로 영상이 전체적(sigma의 분포도가 넓어지기 때문에)을 점점 더 뿌였게 됨.
    # sigma값을 작게하면 -> 물체 주변만 뿌해짐.
cv2.destroyAllWindows()