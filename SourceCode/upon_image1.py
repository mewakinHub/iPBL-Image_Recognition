# upon_image1.py
import cv2
import numpy as np

def main():
    img = cv2.imread('./image/lena512.bmp')
    fimg = cv2.imread('./image/donuts.png')

    print("Lena512:", img.shape)
    print("donuts:", fimg.shape)

    h, w = img.shape[:2] #512x
    fh, fw = fimg.shape[:2] #216x
    img[-fh:h, -fw:w] = fimg

    cv2.imshow("mask", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# run---------------------------------------------------------------------------------------
if __name__ == '__main__':
  main()