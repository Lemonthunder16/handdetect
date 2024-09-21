import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize the hand detector
detector = HandDetector(maxHands=1, detectionCon=0.8)
video = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    success, img = video.read()
    if not success:
        break
    
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)
    
    fing = cv2.imread(r"C:\Projects\HandDetector\f6.jpeg")
    
    if hands:
        hand = hands[0]
        lmlist = hand['lmList']
        
        if lmlist:
            fingerup = detector.fingersUp(hand)
            if fingerup == [0, 1, 0, 0, 0]:
                fing = cv2.imread(r"C:\Projects\HandDetector\f1.jpeg")
            elif fingerup == [0, 1, 1, 0, 0]:
                fing = cv2.imread(r"C:\Projects\HandDetector\f2.jpeg")
            elif fingerup == [0, 1, 1, 1, 0]:
                fing = cv2.imread(r"C:\Projects\HandDetector\f3.jpeg")
            elif fingerup == [0, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Projects\HandDetector\f4.jpeg")
            elif fingerup == [1, 1, 1, 1, 1]:
                fing = cv2.imread(r"C:\Projects\HandDetector\f5.jpeg")
    
    if fing is not None:
        fing = cv2.resize(fing, (220, 280))
        img[50:330, 20:240] = fing
    
    cv2.imshow("Video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
