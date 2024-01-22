import cv2 as cv

cap=cv.VideoCapture(0)
fourcc =cv.VideoWriter_fourcc(*'XVID')
# vddeio save script 
out=cv.VideoWriter('new_video.avi',forcc,20,(640,480))

while(True):
    rect,frame=cap.read()
    if rect ==True:
         #chkeaking frame width and hight 
         print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
         print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
         out.write(frame)

         cv.imshow('frame',frame)
         if cv.waitKey(0) & ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv.destroyAllWindows()
    