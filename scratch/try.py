import cv2

img = cv2.imread("galaxy.jpg", 0)
cv2.imshow("Galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()