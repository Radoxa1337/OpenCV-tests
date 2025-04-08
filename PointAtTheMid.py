import cv2

def CamerasFunc():
    cam = cv2.VideoCapture(0)
    while True:
        ret,frame = cam.read()
        (b,g,r) = frame[frame.shape[1]//2+1, frame.shape[0]//2+1]
        if b>max(g,r):
            b, g, r = 255,0,0
        elif g>max(b,r):
            b, g, r = 0, 255, 0
        else:
            b, g, r = 0, 0, 255
        cv2.rectangle(frame, (frame.shape[1]//2+20, frame.shape[0]//2+100), (frame.shape[1]//2-20, frame.shape[0]//2-100), (int(b), int(g), int(r)), -1)
        cv2.rectangle(frame, (frame.shape[1] // 2 + 100, frame.shape[0] // 2 + 20),(frame.shape[1] // 2 - 100, frame.shape[0] // 2 - 20), (int(b), int(g), int(r)), -1)
        cv2.imshow("output", frame)
        if cv2.waitKey(1)&0xFF == 27:
            break

CamerasFunc()