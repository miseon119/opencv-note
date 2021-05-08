import numpy as np
import cv2

cap = cv2.VideoCapture("out.mp4")
fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
outfile = cv2.VideoWriter('test5.avi', fourcc, 21.0, (1920,1080))
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not(ret):
    	break
	# red_img  = np.full((1080,1920,3), (0,0,255), np.uint8)
    outfile.write(frame)
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    # Quit when 'q' is pressed
    if key == ord('q'):
        break

# When everything done, release the capture
cap.release()
outfile.release();
cv2.destroyAllWindows()
