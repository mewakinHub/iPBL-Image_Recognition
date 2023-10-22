import os
# https://github.com/opencv/opencv/issues/17687
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
device = 0 # camera device number

def takephoto():
    global device

    cap = cv2.VideoCapture(device)
    fps = cap.get(cv2.CAP_PROP_FPS)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("Size:", ht, "x", wt, "/Fps: ", fps)
    while cap.isOpened() :
        ret, frame = cap.read()

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord('s'):
            cv2.imwrite("./image/takephoto.jpg", frame)
        cv2.imshow("video", frame)

    cv2.destroyAllWindows()
    cap.release()

    return frame
    
def main():
    img = takephoto()
    # show image file
    cv2.imshow('window name', img)
    cv2.waitKey(0)  # pause until any key pressed
    cv2.destroyAllWindows()  # close all windows

# The following equation holds when this program file is only executed.
if __name__ == '__main__':
    main() # function name is free