import cv2 as cv

video = cv.VideoCapture('videos/video_2_trial.mov')

subtractor = cv.createBackgroundSubtractorMOG2(30,50)

while True:
    ret, frame = video.read()
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow('Motion Filtering', mask)

        if cv.waitKey(5) == ord('q'):
            break

    else:
        video = cv.VideoCapture('videos/video_2_trial.mov')

cv.destroyAllWindows()
video.release()

