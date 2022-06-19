import numpy as np

import cv2
  
img = cv2.imread('bright.jpg')
cv2.imshow('Original image',img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()


gray.shape
coordinates = cv2.minMaxLoc(gray)
print("coordinates of bright point are",coordinates)



# Window name in which image is displayed
window_name = 'gray'
  
# Center coordinates
center_coordinates = (1590,2324 )
 
# Radius of circle
radius = 20
  
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(gray, center_coordinates, radius, color, thickness)
  
# Displaying the image
cv2.imshow(window_name, image)


# write results
cv2.imwrite("bright_black.jpg", gray)
cv2.imwrite("bright_circle.jpg", image)
