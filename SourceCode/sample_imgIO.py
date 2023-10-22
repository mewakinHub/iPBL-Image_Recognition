# ```python
import cv2

# read image file
img = cv2.imread('./image/standard/Mandrill.bmp')
if img is None:
    print('ERROR: image file is not opened.')
    exit(1)

# write image file
cv2.imwrite('./image/res_scrpt.png', img)

# show image file
cv2.imshow('window name', img)
cv2.waitKey(0)  # pause until any key pressed
cv2.destroyAllWindows()  # close all windows
# ```