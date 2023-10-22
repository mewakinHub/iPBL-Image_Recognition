# myface_dtc_simple.py FaceDetection
# draw face bounding box, face keypoints, and detection score
#just import and use directly from module(so learn form module file)
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
from MediapipeFaceDetection import MediapipeFaceDetection as FaceDect

cap = cv2.VideoCapture(0)
Face = FaceDect()
while cap.isOpened():
    ret, frame = cap.read()
    flipped_frame = cv2.flip(frame, 1)
    Face.detect(flipped_frame)
    annotated_frame = Face.visualize(flipped_frame)
    cv2.imshow('frame', annotated_frame)
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
Face.release()
cap.release()