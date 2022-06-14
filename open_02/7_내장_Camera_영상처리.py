# 동영상 처리하기
# cv2.VideoCapture 클래스
#   - 동영상, 카메라 로부터 frame(프레임) 받아옴
# cv2.VideoCapture(index) ==> retval ( return value)
#    index:0  => 시스템 기본 카메라 (camera_id + domain_offset_id)

# cv2.VideoCapture.isOpened() => retval
# retval 성공하면 T/ 실패시 F

# cv2.VideoCapture.read() => retval, image
# retval => read()  결과 성공하면 T/ 실패시 F
# image => 현재 프레임(영상), numpy.ndarray
# ----------------------------------------------------
import sys
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened(): # 카메라 내용 읽지 못했으면
    print("카메라 사용 안됨.")
    sys.exit()

print('가로 사이즈: ', int( cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈: ', int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:                   # ret => read() 성공하면 TRUE
    ret, frame = cap.read()   # frame => 현재 프레임(영상)

    if not ret: # 성공 못하면
        break
    inversed = ~frame

    cv2.imshow('frame', frame)
    cv2.imshow('inverse', inversed)
    if cv2.waitKey(10) == 27:  # 27: ESC KEY 아스키코드
        break

cap.release()
cv2.destroyAllWindows()
