import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#ended up switching to green for screenshot because when i came back home orange was very hard to find in my room as the surroundings are close to that color
#looked up orange hsv ((28,85,90) and picked this range accordingly
lower_HSV_orange = np.array([50, 100, 100])
higher_HSV_orange = np.array([70,255,255])

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    threshold = cv2.inRange(hsv, lower_HSV_orange, higher_HSV_orange)
    #up until here I have used code from object tracking tutorial
 
    contours,_ = cv2.findContours(threshold, 1, 2)
    # had to add this, if not the program stops when it does't see the colours
    if contours:
	    cnt = contours[0]
	    rect =  cv2.minAreaRect(cnt)
	    box = cv2.boxPoints(rect)
	    box = np.int0(box)
	    cv2.drawContours(frame,[box],0,(0,0,255),2)
    #code above taken from contour tutorial
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
