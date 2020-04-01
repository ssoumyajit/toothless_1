#u can convert mp4 files into avi online n may be then try.
import cv2
import numpy as np
cap = cv2.VideoCapture("elvis.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print(int(fps))
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'FMP4') #FMP4 works yeah ********
#In Windows: DIVX (More to be tested and added)
#In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).

#out = cv2.VideoWriter('yiyasha_video.mp4',cv2.VideoWriter_fourcc('M','J','P','G'),int(fps),(frame_width,frame_height), isColor = False)
out = cv2.VideoWriter('elvis_videoedge.mp4',fourcc,int(fps),(frame_width,frame_height), isColor = False)
while True:
    _, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    #laplacian = cv2.Laplacian(blurred_frame, cv2.CV_64F)
    canny = cv2.Canny(blurred_frame, 100, 150)
    out.write(canny)


    cv2.imshow("Frame", frame)
    #cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Canny", canny)  
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()