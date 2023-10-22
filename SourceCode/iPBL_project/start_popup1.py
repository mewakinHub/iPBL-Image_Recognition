from tkinter import *
import tkinter
from tkinter.messagebox import showerror
import pygame

popup = None

def close_all_windows(callback):
    """Close the rule window and the parent window."""
    popup.destroy()
    if callback:
        callback()

def display_start_popup1(callback, parent):

   global popup
   popup = Toplevel(parent)
    
   x = parent.winfo_x()
   y = parent.winfo_y()
    
   popup.title(" Hey!? Silly🤪")
   # Set the popup's position to be the same as the parent's position
   popup.geometry("800x533+%d+%d" % (x, y))
   popup.resizable(False, False)
   popup.iconbitmap('./image/silly.ico')
   popup.protocol("WM_DELETE_WINDOW", lambda: close_all_windows(callback))


   background_image = PhotoImage(file="background.png")
   background_label = Label(popup, image=background_image)
   background_label.place(relwidth=1, relheight=1)

   message1 = Label(popup, text="Hey!? Silly🤪", fg="white", font=('ZCOOL KuaiLe', 30), bg="#003366", pady=10, anchor="w")
   message1.pack(pady=10)


   message2 = Label(popup, text="Please choose players number", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
   message2.pack(pady=10, fill="x", padx=20)

   def sel():
      selection = "You selected players number: " + str(var.get())
      label.config(text=selection)

   var = IntVar()

   row1 = Frame(popup, bg="#E6E6E6", bd=2, relief="groove")
   row1.pack(pady=5, padx=10)
   row2 = Frame(popup, bg="#E6E6E6", bd=2, relief="groove")
   row2.pack(pady=5, padx=10)
   row3 = Frame(popup, bg="#E6E6E6", bd=2, relief="groove")
   row3.pack(pady=5, padx=10)

   rows = [row1, row2, row3]

   # Using for loop for radiobuttons to avoid repetition
   for i in range(2, 11):  # Loop from 2 to 10 inclusive
       row_num = (i-2) // 3  # This will assign 2,3,4 to row1; 5,6,7 to row2; and 8,9,10 to row3
       Radiobutton(rows[row_num], text=f"{i} players", variable=var, value=i, font=("Courier", 14), command=sel, bg="#E6E6E6", indicatoron=0).pack(side=LEFT, padx=20, anchor=CENTER)

   def nextPage():
      popup.destroy()
      # Import your next module here

   def previousPage():
      popup.destroy()
      parent.deiconify()

   # Button frame to group buttons and control their layout
   button_frame = Frame(popup, bg="#000000")
   button_frame.pack(pady=20, side=BOTTOM, fill=X)

   # Slight padding to separate the buttons
   next_button = Button(button_frame, text="Next", command=nextPage, font=('Helvetica bold', 15))
   next_button.pack(side=RIGHT, padx=10, pady=10)

   back_button = Button(button_frame, text="Back", command=previousPage, font=('Helvetica bold', 15))
   back_button.pack(side=LEFT, padx=10, pady=10)

   label = Label(popup)
   label.pack()

   popup.mainloop()
