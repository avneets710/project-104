import numpy as np
import cv2
black=np.zeros([600,600])
black[200:400,200:400]=255
print(black)
cv2.putText(img,"sun",
            (20,30),
cv2.FONT_HERSHEY_COMPLEX,
0.5,
(255,255,255) 
)
cv2.waitKey(0)
