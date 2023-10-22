import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps
import cv2
import os

# Disable OpenCV hardware transforms to avoid conflicts
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.master.title("OpenCVの動画表示")
        self.master.geometry("400x300")
        
        self.canvas = tk.Canvas(self.master)
        self.canvas.bind('<Button-1>', self.canvas_click)
        self.canvas.pack(expand=True, fill=tk.BOTH)

        self.capture = cv2.VideoCapture(0)
        self.disp_id = None

    def canvas_click(self, event):
        if self.disp_id is None:
            self.disp_image()
        else:
            self.after_cancel(self.disp_id)
            self.disp_id = None

    def disp_image(self):
        ret, frame = self.capture.read()
        cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv_image)
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        pil_image = ImageOps.pad(pil_image, (canvas_width, canvas_height))
        self.photo_image = ImageTk.PhotoImage(image=pil_image)
        self.canvas.delete("all")
        self.canvas.create_image(
            canvas_width / 2,
            canvas_height / 2,
            image=self.photo_image
        )
        self.disp_id = self.after(10, self.disp_image)

def btn_clicked():
    root.title(u'cap your silly face')
    root.geometry('600x600')
    Button = tk.Button(text=u'finish', width=8, height=3, command=takephoto)
    Button.place(x=535, y=550)

def normalFace_set():
    root.title(u'cap your face')
    root.geometry('600x600')
    Button = tk.Button(text=u'next', width=8, height=3, command=btn_clicked)
    Button.place(x=535, y=550)

def destroy_window():
    root.destroy()

def main():
    app = Application(master=root)
    normalFace_set()
    app.mainloop()

def takephoto():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    img = cv2.flip(frame, 1)
    cv2.destroyAllWindows()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img)
    photo_image = ImageTk.PhotoImage(image=pil_image)
    
    # Display the taken photo
    photo_label = tk.Label(root, image=photo_image)
    photo_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    main()
