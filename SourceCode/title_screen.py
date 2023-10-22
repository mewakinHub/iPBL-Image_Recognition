import pygame
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage

# Constants
MAIN_BG_COLOR = "#e1e8f0"
BUTTON_COLOR = "#4a90e2"
BUTTON_FG_COLOR = "black"
TEXT_FONT = ('Helvetica', 35)
BUTTON_FONT = ('Helvetica bold', 25)



def stop_music(music):
    music.stop()
    start_bg.destroy()

def exitApp():
    """Exit the application."""
    stop_music(background_music)

def nextPage():
    start_bg.withdraw()
    import start_popup1
    start_popup1.display_start_popup1(show_main_window, start_bg)

def show_main_window():
    start_bg.deiconify()

def rulePage():
    start_bg.withdraw()
    import rule
    rule.start(show_main_window, parent=start_bg)

if __name__ == "__main__":
    # Initialize main window
    start_bg = Tk()
    start_bg.title(" Hey!? Silly🤪")
    start_bg.geometry("800x533")
    start_bg.resizable(False, False)
    start_bg.iconbitmap('./image/silly.ico')

    # Initialize pygame.mixer for audio
    pygame.mixer.init()

    # Load and play the background music
    background_music = pygame.mixer.Sound("alexander-nakarada-silly-intro(chosic.com).mp3")
    background_music.play(loops=-1)  

    # Set background image
    background_image = PhotoImage(file="background.png")
    background_label = Label(start_bg, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Add text label
    label1 = Label(start_bg, text="Hey!? Silly🤪",fg="white", font=('ZCOOL KuaiLe', 30), bg="#003366", pady=10, anchor="w")
    label1.pack(pady=25)

    # Configure button styles
    style = ttk.Style()
    style.configure("TButton", background=BUTTON_COLOR, foreground=BUTTON_FG_COLOR, font=BUTTON_FONT)

    # Create & show buttons
    button1 = ttk.Button(start_bg, text="PLAY", command=nextPage, style="TButton")
    button1.pack(pady=20)
    
    button2 = ttk.Button(start_bg, text="RULE", command=rulePage, style="TButton")
    button2.pack(pady=20)

    exit_button = Button(start_bg, text="Exit", command=exitApp, font=('Helvetica bold', 15), bg="#ff4d4d", fg="white")
    exit_button.place(x=730, y=490)

    # Stop the music when the window is closed
    start_bg.protocol("WM_DELETE_WINDOW", lambda: stop_music(background_music))

    start_bg.mainloop()
