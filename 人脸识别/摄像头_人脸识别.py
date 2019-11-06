import cv2
detector_face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # 更改画面效果
    # frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    faces = detector_face.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Camera', frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("s"):
        cv2.imwrite("asd.png", frame)
cap.release()
cv2.destroyAllWindows()
