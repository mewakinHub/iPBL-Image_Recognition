import os
# https://github.com/opencv/opencv/issues/17687
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

device = 0 # camera device number
# device = "./image/moviefile.avi"

# main----------------------------------------------------
def main():
    global device

    cap = cv2.VideoCapture(device)
    fps = cap.get(cv2.CAP_PROP_FPS)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("Size:", ht, "x", wt, "/Fps: ", fps)
    while cap.isOpened() :
        ret, frame = cap.read()
        # 1st return value is a boolean value for whether success in reaing a frame
        # 2nd return value is the list of the pixel values in a frame

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # wait 1 ms then continue while loop (done if bc next line)
        # if cv2.waitKey(int(1000/fps)) & 0xFF == ord('q'):
        # is better way to only wait frame by frame
        cv2.imshow("video", frame)

    cv2.destroyAllWindows()
    cap.release()

# run-----------------------------------------------------
if __name__ == '__main__':
    main()