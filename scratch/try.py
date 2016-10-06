import cv2

img = cv2.imread("galaxy.jpg", 0)
resized_image = cv2.resize(img, (int(img.shape[1]/4),int(img.shape[0]/4)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_small.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()