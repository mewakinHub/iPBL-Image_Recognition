from tkinter import *

# Global variables
rule_window = None
background_image = None

def close_all_windows(callback):
    """Close the rule window and the parent window."""
    rule_window.destroy()
    if callback:
        callback()

def go_to_title_screen(callback):
    """Close the rule window and execute the provided callback."""
    rule_window.destroy()
    callback()

def start(callback, is_main=False, parent=None):
    global rule_window, background_image

    if rule_window:
        rule_window.destroy()

    if is_main:
        rule_window = Tk()
    else:
        rule_window = Toplevel(parent)
        # Get the parent window's position and set it to the Toplevel window
        x = parent.winfo_x()
        y = parent.winfo_y()
        rule_window.geometry("800x533+%d+%d" % (x, y))
    rule_window.title("Rule of Game")
    rule_window.resizable(False, False)
    rule_window.iconbitmap('./image/silly.ico')
    rule_window.protocol("WM_DELETE_WINDOW", lambda: close_all_windows(callback))

    # Set the background
    background_image = PhotoImage(file="background.png")
    background_label = Label(rule_window, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    # Create rule text labels
    label_title = Label(rule_window, text="Rule of game", fg="white", font=('Arial bold', 30), bg="#003366", pady=10, anchor="w")
    label_rule1 = Label(rule_window, text="1. Choose players number.", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
    label_rule2 = Label(rule_window, text="2. First, a player decides to act the silly face.", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
    label_rule3 = Label(rule_window, text="3. Next, the player imitates from the previous player.", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
    label_rule4 = Label(rule_window, text="4. Compete for the score between the first and the last player.", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
    label_rule5 = Label(rule_window, text="ex. Don't use own hands", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")
    label_rule6 = Label(rule_window, text="ex. The more you face the front, the more accurate you are.", fg="black", font=('Arial', 18), bg="#E6E6E6", pady=5, bd=1, relief="solid", anchor="w")

    # Display the labels
    label_title.pack(pady=10)  # padx is added to give some space from the window's left edge
    label_rule1.pack(pady=10, fill="x", padx=20)
    label_rule2.pack(pady=10, fill="x", padx=20)
    label_rule3.pack(pady=10, fill="x", padx=20)
    label_rule4.pack(pady=10, fill="x", padx=20)
    label_rule5.pack(pady=10, fill="x", padx=20)
    label_rule6.pack(pady=10, fill="x", padx=20)

    # Button frame to group the Back button and control its layout
    button_frame = Frame(rule_window, bg="#000000")
    button_frame.pack(pady=20, side=BOTTOM, fill=X)

    back_button = Button(button_frame, text="Back", command=lambda: go_to_title_screen(callback), font=('Helvetica bold', 15))
    back_button.pack(side=LEFT, padx=(10, 0), pady=10, expand=True)

    if is_main:
        rule_window.mainloop()

if __name__ == "__main__":
    start(None, is_main=True)
