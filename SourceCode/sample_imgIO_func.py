import cv2
a = 1 # global variable

def imageIO(img_name_in, img_name_out):
    # read image file
    img = cv2.imread(img_name_in)
    if img is None:
        print('ERROR: image file is not opened.')
        exit(1)

    # write image file
    cv2.imwrite(img_name_out, img)
    return img

def main():
    print(a, b) # print global variables
    in_name = './image/standard/Mandrill.bmp' # local variable
    out_name = './image/res_func1.png' # local variable
    img = imageIO(in_name, out_name)
    # show image file
    cv2.imshow('window name', img)
    cv2.waitKey(0)  # pause until any key pressed
    cv2.destroyAllWindows()  # close all windows

# The following equation holds when this program file is only executed.
if __name__ == '__main__':
    b = 0 # global variable
    main() # function name is free
