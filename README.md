
#OpenCV Motion Filtering
_First of All install OpenCV_

```
pip install opencv-python
```

Create A file called `Project_one.py`

**Make Sure you have a vide file**  
[Here](https://www.youtube.com/watch?v=ORrrKXGx2SE) is a video on youtube you have to download  
You can name it `Project_one_video.mp4`
###Step Wise Guide on how to do  

Import open-cv  
```python
import cv2 as cv
```
Make a _variable_ `video` 
```python
video = cv.VideoCapture('Project_one_video.mp4')
```
Note you could use your camera too

```python
video = cv2.VideoCapture(0)
```

Create a subtractor object
```python
subtractor = cv.createBackgroundSubtractorMOG2(20,50)
```

Now Lets create a while loop that reads the video and capture the two values the read function returns  
```python
while True:
    ret, frame = video.read()
```

If the `ret`, the return value exists 

```python
    if ret:
        mask = subtractor.apply(frame)
        cv2.imshow('Motion Filtering', mask)
```

Add waitkey

```python
    if ret:
        mask = subtractor.apply(frame)
        cv2.imshow('Motion Filtering', mask)

        if cv.waitKey(5) == ord('q'):
            break
```
Finally Destroy all windows and release the video
```python
cv.destroyAllWindows()
video.release()
```

#View the Complete Code Below
```python
import cv2 as cv

video = cv.VideoCapture('Project_one_video.mp4')

subtractor = cv.createBackgroundSubtractorMOG2(20,50)

while True:
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Motion Filtering', mask)

        if cv.waitKey(5) == ord('q'):
            break

    else:
        video = cv.VideoCapture('Project_one_video.mp4')

cv.destroyAllWindows()
video.release()


```
