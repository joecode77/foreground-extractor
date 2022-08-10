import cv2
import numpy as np

img_with_fgd = cv2.imread("Images/extract_minion.jpg")
img_with_bgd = cv2.imread("Images/background.jpg")

img_with_bgd = cv2.resize(img_with_bgd, (img_with_fgd.shape[1], img_with_fgd.shape[0]))
mask = np.zeros(img_with_bgd.shape[:2])

rect = (322, 338, 728, 823)

bgdModel = np.zeros((1, 65), dtype = np.float64)
fgdModel = np.zeros((1, 65), dtype = np.float64)

mask, bgdModel, fgdModel = cv2.grabCut(img_with_fgd, mask, rect, bgdModel, fgdModel, iterCount = 10, mode = cv2.GC_INIT_WITH_RECT)

mask = np.where((mask == cv2.GC_BGD) | (mask == cv2.GC_PR_BGD), 0, 1)
output_mask = (mask * 255).astype(np.uint8)

extracted_fgd = cv2.bitwise_and(img_with_fgd, img_with_fgd, mask = output_mask)

final_image = cv2.addWeighted(extracted_fgd, 1, img_with_bgd, 0.4, 0)

cv2.imshow("Image", img_with_fgd)
cv2.imshow("Intermediate Image", extracted_fgd)
cv2.imshow("Final Image", final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
