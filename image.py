#!/usr/bin/python2

import  cv2

#  laoding  image 
img=cv2.imread('Dice.jpg')

#  Print  height and width
#print  Dice.shape

#  to display that image 
cv2.imshow("Dice",img)
#cv2.imshow("dognew",img1)

#  image window holder activate 
cv2.waitKey(0)
#  waitkey will destroy  by using  q  button
cv2.destroyAllWindows()

