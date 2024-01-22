import cv2 as cv
import numpy as np 
# creat zeroo image 
img=np.zeros([560,600,3],np.uint8)

# drawing line
img=cv.line(img,(0,0),(260,260),(255,0,0),10)

# drawing arrowdline
img=cv.arrowedLine(img,(300,0),(400,400),(0,0,255),20)

#creat rectangle
img=cv.rectangle(img,(300,0),(200,80),(0,255,0),5)
# creat circle
img=cv.circle(img,(100,100),90,(0,0,255),-1)
# put on text 
font=cv.FONT_HERSHEY_SIMPLEX
img=cv.putText(img,'Jahid',(150,360),font,5,(0,0,255),5,cv.LINE_AA)

#frame=cv.imread(img)

cv.imshow('frame',img)
if cv.waitKey(0) & 0xFF ==ord('q'):
    cv.destroyALlWindows()


