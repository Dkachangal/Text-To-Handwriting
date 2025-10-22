import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('p3.jpg')
img1Grey = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(img1Grey, 150, 255, cv2.THRESH_BINARY)

plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.imshow(img1Grey, cmap = 'gray')

contours1, heirarchy1 = cv2.findContours(image = thresh1, mode = cv2.RETR_TREE, method= cv2.CHAIN_APPROX_NONE)
# print(heirarchy1)

img_contours1 = cv2.drawContours(image = img1.copy(), contours=contours1, contourIdx=-1, color=(255,0,0), thickness=1, lineType = cv2.LINE_AA)
plt.imshow(img_contours1)
plt.show()
