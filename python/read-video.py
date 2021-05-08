import numpy as np
import cv2

cap = cv2.VideoCapture("out.mp4")
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not(ret):
    	break
	# red_img  = np.full((1080,1920,3), (0,0,255), np.uint8)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(0)
    # show one frame at a time
    while key not in [ord('q'), ord('k')]:
        key = cv2.waitKey(0)
    # Quit when 'q' is pressed
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
# outfile.release();
cv2.destroyAllWindows()
