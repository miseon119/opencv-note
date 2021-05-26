import numpy as np
import cv2

img = np.zeros((500,500,3), np.uint8)

# draw rectangle
img = cv2.rectangle(img, (100,100), (200, 200), (0,0,255),3)

# draw line
img = cv2.line(img, (50,50), (200, 200), (0,0,255),3)

# draw contour
cv2.drawContours(drawing, hull, i, color, 1, 8)

# draw text
cv2.putText(img, 'OpenCV', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2)
