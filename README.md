# OpenCV-Note

### OpenCV Version Check 

**Python**
```python
import cv2
cv2.__version__
```

**C++**

In terminal:
```console
$ pkg-config --modversion opencv4
```
or 
```console
$ pkg-config --modversion opencv
```

## Python

| # | Title | Description | Reference |
|---| ----- | ----------- | --------- |
|1| [Read Video](./python/read-video.py)|  | |
|2| [Write Video](./python/write-video.py)|  | |
|3| [Scale contour](./python/contour/scale-contour.py)| Resize contour, Translating the contour by subtracting the center with all the points | [More detail](https://medium.com/analytics-vidhya/tutorial-how-to-scale-and-rotate-contours-in-opencv-using-python-f48be59c35a2) |
|4| [Rotate contour](./python/contour/rotate-contour.py)| Convert the points to polar co-ordinates, add the rotation, and convert it back| [More detail](https://medium.com/analytics-vidhya/tutorial-how-to-scale-and-rotate-contours-in-opencv-using-python-f48be59c35a2) | 
|5| [Draw](./python/draw.py)| Draw line, rectangle, contour | |
