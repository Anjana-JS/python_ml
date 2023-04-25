import cv2
vid = cv2.VideoCapture(0)
while True:
    ret, img = vid.read()
    image = cv2.putText(img,"Python Video Capturing Tutorial",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(200,20,50),2)
    cv2.imshow("Live",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
