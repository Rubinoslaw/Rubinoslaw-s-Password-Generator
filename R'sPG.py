# Rubinosław's Password Generator

from tkinter import *
from random import randint
import webbrowser

root = Tk()
root.title("Rubinosław's Password Generator")
root.geometry("777x777")
root.configure(bg="#003300")
root.resizable(True, True)

def password_generate():
    # Clear of Entry Box
    pw_entry.delete(0, END)
    # Password
    pw_lenght = int(my_entry.get())
    my_password = ''

    for x in range(pw_lenght):
        my_password += chr(randint(33, 126))
        # Output password to the program
        pw_entry.insert(0, my_password)

def github():
    webbrowser.open("https://github.com/Rubinoslaw")

# Label Things
lf = LabelFrame(root, text="How Many Characters You Want for Your Password?", bg="#003300", fg="white")
lf.pack(pady=20)

# Number of Charcters Entry Box
my_entry = Entry(lf, font=("Minion Pro Med", 22))
my_entry.pack(pady=30, padx=30)
pw_entry = Entry(root, text="", font=("Minion Pro Med", 22))
pw_entry.pack(pady=30)

# Buttons
my_frame = Frame(root)
my_frame.pack(pady=30)
button = Button(my_frame, text="Generate Strong Password", bg="white", command=password_generate)
button.grid(row=0, column=0, padx=12)

my_frame = Frame(root)
my_frame.pack(pady=30)
github_button = Button(my_frame, text="GitHub", bg="white", command=github)
github_button.grid(row=0, column=0, padx=12)


root.mainloop()