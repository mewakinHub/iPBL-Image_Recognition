# Sample of video-image recorder
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

device = 0 # camera device number
video_name = "record.avi"

# main----------------------------------------------------
def main():
    global device, video_name
    recflag = False

    cap = cv2.VideoCapture(device)
    fps = cap.get(cv2.CAP_PROP_FPS)
    wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    print("Size:", ht, "x", wt, "/Fps: ", fps)

    writer = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*"H264"), fps, (int(wt), int(ht)))

    while cap.isOpened() :
        ret, frame = cap.read()
        if recflag:
            writer.write(frame)
            cv2.circle(frame, (20, 20), 5, [0,0,255], -1)
            # red circle record symbol

        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('r'):
            recflag = ~recflag # `~` is inversion. (True->False, False->True)

        cv2.imshow("video", frame)

    if writer.isOpened():
        writer.release()
    cv2.destroyAllWindows()
    cap.release()

# run-----------------------------------------------------
if __name__ == '__main__':
    main()