# upon_image2.py
import cv2
import numpy as np

def main():
    lena  = cv2.imread('./image/lena512.bmp')
    dnts  = cv2.imread('./image/donuts.png')
    white = np.ones_like(lena) * 255 #make a matrix whose size and type are the same as lena
    #*255 to make it white on all pixel of lena's size

    h, w = lena.shape[:2] #512x
    fh, fw = dnts.shape[:2] #216x
    white[-fh:h,-fw:w] = dnts

    print([white!=[255,255,255]])

    lena[white!=[255, 255, 255]] = white[white!=[255, 255, 255]]

    cv2.imshow("mask", lena)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# run---------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()