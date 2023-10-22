import cv2
# if terminal is sourcecode then just use ./(current directory)
# ../ mean out of current directory
def main():
    img = cv2.imread("./image/standard/Lenna.bmp")
    print("H x W x Color Channel", img.shape)

    cv2.imshow("image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # write image file
    cv2.imwrite('./image/res_scrpt.png',img) 
    #saving an image to a file in various formats

if __name__=='__main__':
    main()