#importing openCv
import cv2
#opening image in pwd using imread
image=cv2.imread('cat.png')
#changing the format of the open image and saving a new copy
cv2.imwrite('edited_pic.jpg',image)
#opening image in grayscale format
edited_grey=cv2.imread('edited_pic.jpg',cv2.IMREAD_GRAYSCALE)
#saving the grey scale image.
cv2.imwrite('grey_cat.jpg',edited_grey)
