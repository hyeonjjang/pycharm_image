import sys
import cv2

cap = cv2.VideoCapture('Blossoms.mp4')
if not cap.isOpened():
    print("동영상 재생 안됨.")
    sys.exit()

print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('프레임수: ', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS :', fps)
delay = round(1000 / fps)  #33.3초 재생
print('delay :', delay)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    inversed =  ~frame
    cv2.imshow('Frame',frame)
    cv2.imshow('inverse',inversed)
    if cv2.waitKey(delay) == 27: # ESC 누르면 벗어남
        break
cap.release()
cv2.destroyAllWindows()


