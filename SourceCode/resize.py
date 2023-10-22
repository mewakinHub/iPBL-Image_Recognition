import cv2

def resizeImg(img, length):
    """
    This function resizes the long side of images to the specified length while keeping the aspect ratio.

    Args:
        img(numpy.ndarray): input image
        length(int): length of long side after resizing

    Returns:
        numpy.ndarray: resized image
    """
    h, w = img.shape[:2] #slicing index0 to (2-1)
    if max(h, w) < length:
        return img
    if h < w:
        newSize = (int(h*length/w), length)
    else:
        newSize = (length, int(w*length/h))
    print('resize to', newSize)
    return cv2.resize(img, (newSize[1], newSize[0])) # (w, h)

def main():
    in_name = './image/standard/Mandrill.bmp'
    img = cv2.imread(in_name)
    if img is None:
        print('ERROR: image file is not opened.')
        exit(1)

    img150x100 = cv2.resize(img, (150, 100)) #dsize = tuple(x,y)
    img_half = cv2.resize(img, None, fx=2/3, fy=2/3) #scaling
    img150 = resizeImg(img.copy(), 150) #same aspectRatio

    cv2.imshow('img', img)
    cv2.imshow('img150x100', img150x100)
    cv2.imshow('img_half', img_half)
    cv2.imshow('img150', img150)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()