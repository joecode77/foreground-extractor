import numpy as np
import argparse
import cv2
import os

argumentParser = argparse.ArgumentParser()
argumentParser.add_argument("-f", "--fore", type = str, default = "Images/extract_minion.jpg", help = "The image containing the foreground")
argumentParser.add_argument("-b", "--back", type = str, default = "Images/background.jpg", help = "The image containing the background")
argumentParser.add_argument("-r", "--rect", type = str, default = "322, 338, 728, 823", help = "The rectangle that defines the region containing the foreground. Entered as a string separated by commas")

parameters = vars(argumentParser.parse_args())


def extract_foreground(*args, **kwargs):
    
    img_with_fgd = cv2.imread(kwargs.get("fore"))
    img_with_bgd = cv2.imread(kwargs.get("back"))
    img_with_bgd = cv2.resize(img_with_bgd, (img_with_fgd.shape[1], img_with_fgd.shape[0]))
    mask = np.zeros(img_with_bgd.shape[:2])
    
    rect = []
    split_rect = kwargs.get("rect").split(",")

    for i in split_rect:
        if i.strip().isdigit():
            rect.append(int(i.strip()))
        else:
            print(f"[ERROR]: Not all elements of {split_rect} is a number. All the elements of --rect must be a number.")
            quit()
    rect = tuple(rect)

    if len(rect) != 4:
        print(f"[ERROR]: {rect} does not contain four digits. It should contain only four digits separated by commas.")
        quit()

    

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

fore = parameters.get("fore")
back = parameters.get("back")

if not os.path.isfile(back):
    print(f"[ERROR]: {fore} is not a valid file path")
 
elif not os.path.isfile(fore):
    print(f"[ERROR]: {back} is not a valid file path")

else:
    extract_foreground(**parameters)
