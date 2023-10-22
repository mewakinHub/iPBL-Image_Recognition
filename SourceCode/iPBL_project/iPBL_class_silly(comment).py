import os
import cv2
from MediapipeFaceLandmark import MediapipeFaceLandmark as FaceLmk  #from module import class as abbreviation

class FaceRecognition:
    def __init__(self, playerNumber):
        # Initialize your variables and Mediapipe Face
        self.Face = FaceLmk()
        self.silly_faces = []
        self.straight_faces = []
        self.diff = [] #expression
        self.playerNumber = playerNumber
        # 0:forehead 1:l-cheek 2:r-cheek 3:chin 4:mouth(upper ripp) 5: l-eye 6:r-eye
        # test parts
        self.WIDTH = 1080
        self.HEIGHT = 720
        # keypoints of parts
        self.FACE_PARTS = [ #2D Matrix
            [139, 71, 68, 104, 69, 108, 151, 337, 299, 333, 298, 301, 368, 156, 70, 63, 105, 66, 107, 9, 336, 296, 334, 293, 300, 383, 34, 143, 35, 124, 46, 53, 52, 65, 55, 8, 285, 295, 282, 283, 276, 353, 265, 372, 264],
            [266, 330, 347, 346, 340, 372, 264, 356, 454, 323, 426, 436, 432, 434, 364, 367, 397, 288, 361, 345, 447, 425, 411, 376, 433, 401, 280, 352, 366, 427, 416, 435],
            [93, 234, 127, 34, 143, 111, 117, 118, 101, 36, 132, 58, 172, 138, 135, 214, 212, 216, 206, 227, 116, 177, 213, 147, 187, 205, 137, 123, 50, 215, 192, 207],
            [43, 106, 182, 83, 18, 313, 406, 335, 273, 202, 204, 194, 201, 200, 421, 418, 424, 422, 210, 211, 32, 208, 199, 428, 262, 431, 430, 169, 170, 140, 171, 175, 396, 369, 395, 394, 95, 88, 178, 87, 14, 317, 402, 318, 324, 146, 91, 181, 84, 17, 314, 405, 321, 375, 96, 89, 179, 86, 15, 316, 403, 319, 325, 77, 90, 180, 85, 16, 315, 404, 320, 307],
            [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291, 78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308, 76, 184, 74, 73, 72, 11, 302, 303, 304, 408, 306, 62, 183, 42, 41, 38, 12, 268, 271, 272, 407, 292, 186, 92, 165, 167, 164, 393, 391, 322, 410],
            [466, 388, 387, 386, 385, 384, 398, 263, 249, 390, 373, 374, 380, 381, 382, 362, 467, 260, 259, 257, 258, 286, 414, 359, 255, 339, 254, 253, 252, 256, 341, 463, 342, 445, 444, 443, 442, 441, 413, 446, 261, 448, 449, 450, 451, 452, 453, 464, 383, 300, 293, 334, 296, 336, 285, 417, 265, 353, 276, 283, 282, 295],
            [246, 161, 160, 159, 158, 157, 173, 33, 7, 163, 144, 145, 153, 154, 155, 133, 247, 30, 29, 27, 28, 56, 190, 130, 25, 110, 24, 23, 22, 26, 112, 243, 113, 225, 224, 223, 222, 221, 189, 226, 31, 228, 229, 230, 231, 232, 233, 244, 156, 70, 63, 105, 66, 107, 55, 193, 35, 124, 46, 53, 52, 65],
        ]

        self.KEY = [[1,10], [1, 10], [1, 10], [1, 10], [1,10], [130, 243], [359, 362]] #eyelash in-out for each eye

    def caluclate_distance(self, point1, point2): #Pytagorus
        return ((point1.x-point2.x) * self.WIDTH) ** 2 + ((point1.y-point2.y) * self.HEIGHT) ** 2

    def takephoto(self, mode):
        device = 0
        cap = cv2.VideoCapture(device)
        wt  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        ht  = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        while cap.isOpened() :
            ret, frame = cap.read() #copied DataFrame
            img = cv2.ellipse(frame.copy(), center=(int(wt/2), int(ht/2)), axes=(int(wt/4), int(ht/2.2)), angle=0, startAngle=0, endAngle=360, color=(255, 255, 255))
            cv2.line(img, pt1=(int(wt/2), 0), pt2=(int(wt/2), int(ht)), color=(255, 255, 255)) #cross line
            cv2.line(img, pt1=(0,int(ht/5 * 3)), pt2=(int(wt), int(ht/5 * 3)), color=(255, 255, 255)) 
            cv2.putText(img, 'Fit your face to the guidline', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            if mode == 'silly':
                cv2.putText(img, 'Please make silly face', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            else:
                cv2.putText(img, 'Please make straight face', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)


            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                exit()
            elif key & 0xFF == ord('s'):
                img = cv2.flip(frame, 1)
                break
            cv2.imshow("video", img)

        cv2.destroyAllWindows()
        cap.release()

        return img

    def noramlization(self, face):  #[each column in row] for each row
        distance = [[0 for _ in range(len(self.FACE_PARTS[i]))] for i in range(len(self.FACE_PARTS))] #0 in 2D matrix
        for i in range(len(self.FACE_PARTS)):   #each List in Nested list
            normal = self.caluclate_distance(face[self.KEY[i][0]], face[self.KEY[i][1]]) #normal line
            for index, j in enumerate(self.FACE_PARTS[i]):  #each column[Enumerated Obj = index & j('value of index')]
                distance[i][index] = self.caluclate_distance(face[self.KEY[i][0]], face[j]) #refKey vs faceKey
                distance[i][index] /= normal    #overwrite 0 list(distance)

        return distance

    def caluclate_diff(self, distance1, distance2):
        result = [[0 for _ in range(len(self.FACE_PARTS[i]))] for i in range(len(self.FACE_PARTS))]
        for i in range(len(self.FACE_PARTS)):
            for j in range(len(self.FACE_PARTS[i])):
                result[i][j] =  distance1[i][j] - distance2[i][j]   #diff f 2 distance
        return result

    def calculate_score(self, diff1, diff2):
        diff_sum = [0 for _ in range(len(self.FACE_PARTS))] #of very face component list
        for i in range(len(self.FACE_PARTS)):
            for j in range(len(self.FACE_PARTS[i])):
                diff_sum[i] +=  abs(diff1[i][j] - diff2[i][j])

        score = 0
        for i in range(len(self.FACE_PARTS)):
            if(i>4):    # 5: l-eye 6:r-eye
                if(diff_sum[i] < 50):
                    score += 1000 * (50-diff_sum[i])
            elif(i==0): # 0:forehead
                if(diff_sum[i] < 5):
                    score += 10000 * (5-diff_sum[i])
            elif(i==2 or i==3): #??ask musashi
                if(diff_sum[i] < 5):
                    score += 20000 * (5-diff_sum[i])
            else:   #index = 1 1:l-cheek, i= 2:r-cheek
                if(diff_sum[i] < 5): #0:forehead 1:l-cheek 2:r-cheek 3:chin 4:mouth(upper ripp)
                    score += 15000 * (5-diff_sum[i])
        return score

    def main(self):
        for i in range(self.playerNumber): #repeat No. of player
            self.straight_faces.append(self.takephoto('noraml')) #photo
            self.silly_faces.append(self.takephoto('silly'))
            straight_detect = self.Face.detect(self.straight_faces[i]) #detect face mesh
            silly_detect = self.Face.detect(self.silly_faces[i])
            straight_result = self.noramlization(straight_detect.face_landmarks[0]) #normalize distance*
            silly_result = self.noramlization(silly_detect.face_landmarks[0])

            self.diff.append(self.caluclate_diff(straight_result, silly_result)) #cal expression*

        score = self.calculate_score(self.diff[0], self.diff[1])    #compare to get score*
        print(score)

        self.Face.release()

if __name__ == '__main__':
    face_recog = FaceRecognition(2)
    face_recog.main()
