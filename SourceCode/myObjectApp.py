import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import mediapipe as mp


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        frame = tkinter.Frame(master=window,bg="skyblue",padx=10)
        frame.pack()
        self.video_source = video_source
        self.is_recognition_enabled = False
        self.recognized_gesture = None
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
 
        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.pack()
 
        # Button that lets the user take a snapshot
        self.btn_start=tkinter.Button(window, text="Start Signing", width=50, command=self.start,state=tkinter.NORMAL)
        
        self.btn_stop=tkinter.Button(window,text="End Message",width=50,command=self.stop)
        self.btn_stop["state"] = tkinter.DISABLED

        self.result_label = tkinter.Label(window,text="Result: ",font=('Calibri 15 bold'))
        self.result_label.pack(anchor=tkinter.CENTER,expand=True)

        self.btn_start.pack(anchor=tkinter.CENTER, expand=True)
        self.btn_stop.pack(anchor=tkinter.CENTER, expand=True)

        self.timestamp = 0
        self.__create_recognizer()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 100  # Increase the delay (e.g., 100 milliseconds)
        self.update()
        self.window.mainloop()
 
    def start(self):
        self.btn_start["state"] = tkinter.DISABLED
        self.btn_stop["state"] = tkinter.NORMAL
        self.is_recognition_enabled = True

    def result_callback(self, result, output_image, timestamp_ms):
        first_gesture = "No gestures"
        if len(result.gestures) > 0:
            first_gesture = "Category: " + result.gestures[0][0].category_name
            print(f"First recognized gesture: {first_gesture}")
        self.recognized_gesture = first_gesture

    """
    def __create_recognizer(self): # recognizer should be created only once
        BaseOptions = mp.tasks.BaseOptions
        GestureRecognizer = mp.tasks.vision.GestureRecognizer
        GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
        VisionRunningMode = mp.tasks.vision.RunningMode
        # Create a gesture recognizer instance with the live stream mode:
        options = GestureRecognizerOptions(
                base_options=BaseOptions(model_asset_path='./models/gesture_recognizer.task'),
                running_mode=VisionRunningMode.LIVE_STREAM,
                result_callback=self.result_callback)
        self.recognizer = GestureRecognizer.create_from_options(options)

    def recognize(self, img):
        SIZE = 64   #USING THE SNAPSHOT, RESIZING AND PUTTING THROUGH MODEL
        img = cv2.resize(img, (SIZE, SIZE))
        flip = cv2.flip(img, 1)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=flip)
        # STEP 3: Recognize gestures in the input image.
        self.recognizer.recognize_async(mp_image, self.timestamp) # returns None
        # timestamp must be *always* monotonically increasing (otherwise exception)
        # this is required due to LIVE_STREAM mode
        self.timestamp = self.timestamp + 1 
        """
    def __create_recognizer(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_objectron = mp.solutions.objectron

        self.drawing_spec = mp_drawing.DrawingSpec(thickness=2, circle_radius=1)

        self.objectron = mp_objectron.Objectron(
            static_image_mode=False,
            max_num_objects=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def recognize(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.objectron.process(img_rgb)

        if results.detected_objects:
            for detected_object in results.detected_objects:
                mp_drawing.draw_landmarks(
                    img,
                    detected_object.landmarks,
                    mp_objectron.BOX_CONNECTIONS,
                    landmark_drawing_spec=self.drawing_spec,
                    connection_drawing_spec=self.drawing_spec,
                )
            self.recognized_gesture = f"Object: {results.detected_objects[0].class_name}"
        else:
            self.recognized_gesture = "No object detected"


    def stop(self):
        self.is_recognition_enabled = False
        self.btn_stop["state"] = tkinter.DISABLED
        self.btn_start["state"] = tkinter.NORMAL
        self.result_label.config(text="Stopped")
            
    # def update(self):
    #     # Get a frame from the video source
    #     ret, frame = self.vid.get_frame()
    #     if ret:
    #         self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    #         self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
    #         if self.is_recognition_enabled:
    #             self.recognize(frame)   
    #             self.result_label.config(text=self.recognized_gesture)

    #     self.window.after(self.delay, self.update)

    def update(self):
    # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

            if self.is_recognition_enabled:
                self.recognize(frame)
                self.result_label.config(text=self.recognized_gesture)

        self.window.after(self.delay, self.update)
    

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
 
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
 
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)
 
    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

    
#Create a window and pass it to the Application object
App(tkinter.Tk(), "ASL Interpreter")