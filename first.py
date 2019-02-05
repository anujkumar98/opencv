import cv2
image=cv2.imread('cat.png')
cv2.imwrite('edited_pic.jpg',image)
edited_grey=cv2.imread('edited_pic.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('grey_cat.jpg',edited_grey)
