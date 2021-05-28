import cv2

contours, hierarchy = cv.findContours(img_binary, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# iterate contour and draw
for cnt in contours:
  cv2.drawContours(img, contours, -1, (0,0,255), 1)
  
# calculate contour area 
area = cv.contourArea(cnt)

# approximate contour
epsilon = 0.02 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)

# calculate contour center
for cnt in contours:
    M = cv.moments(cnt)
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    cv.circle(img_color, (cx, cy), 10, (0,0,255), -1)
    
# Get bounding rectangle
x, y, w, h = cv.boundingRect(cnt)

# Get rotated rectangle
rect = cv.minAreaRect(cnt)
box = cv.boxPoints(rect)
box = np.int0(box)

# get convex hull shape
hull = cv.convexHull(cnt)

# Convexity defects
hull = cv.convexHull(cnt, returnPoints = False)
defects = cv.convexityDefects(cnt, hull)


# minimum enclosing circle
(x,y), radius = cv2.minEnclosingCircle(cnt)
center=(int(x), int(y))
radius=int(radius)

# fitting an ellipse
ellipse = cv2.fitEllipse(cnt)
img=cv2.ellipse(img, ellipse, (0,255,0),2)

# fitting a line
[vx,vy,x,y] = cv2.fitLine(max_contour,cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((img_gray.shape[1]-x)*vy/vx)+y)
PT1 = (0,lefty)
PT2 = (img_gray.shape[1]-1,righty)
