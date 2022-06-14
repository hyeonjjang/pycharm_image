import sys
import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("카메라 열 수 없음")
    sys.exit()

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
#  ------- 동영상 저장하기 --------
# 원하는 프레임으로 동영상 저장 => 프레임: 원본크기, 데이터타입 같아야함       (부호화+복호화)
# fourcc(4-문자코드, four character code)                  Codec  =  coder + decoder
fourcc = cv2.VideoWriter_fourcc(*'DIVX')    # DIVX: MPEG-4 코덱
delay  = round(1000/fps)

#                          파일이름   fourcc객체  초당프레임  프레임 크기 + (색 TRUE:컬러, FALSE:흑백)
out    = cv2.VideoWriter('output.avi', fourcc,     fps,     (w, h))
if not out.isOpened():
    print("파일을 열 수 없습니다")
    cap.release()
    sys.exit()
while True:
    ret, frame = cap.read()
    if not ret:
        break
    inversed = ~frame
    out.write(frame) # or out.write(inversed)
    cv2.imshow('frame', frame)
    cv2.imshow('inverse', inversed)
    if cv2.waitKey(delay) == 27:
        break
# -------------------------------
cap.release()
out.release()
cv2.destroyAllWindows()
# open_03 폴더에 output.avi 동영상 저장됨