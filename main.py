import os
import shutil
from tkinter import messagebox
from tkinter import *


def declutter():
    location = folder_entry.get()
    reply = messagebox.askokcancel(title="Confirm", message="Declutter folder?")
    if reply:
        items = os.listdir(location)

        files_folder = f"{location}/Files"
        try:
            os.mkdir(files_folder)
        except FileExistsError:
            pass

        try:
            os.mkdir(f"{location}/Folders")
        except FileExistsError:
            pass

        for item in items:
            if os.path.isfile(f"{location}/{item}"):
                shutil.move(f"{location}/{item}", files_folder)
            else:
                if not item == "Files":
                    shutil.move(f"{location}/{item}", f"{location}/Folders")
    quit()


window = Tk()
window.title("File Sorter")
window.config(padx=40, pady=40)
entry_text = Label(text="Enter folder location to declutter: ", pady=30, font=("Arial", 20))
entry_text.pack()
folder_entry = Entry(width=50)
folder_entry.pack()
frame = Frame(bd=1)
frame.pack(fill='both', expand=True, pady=30)
declutter_button = Button(frame, text="Sort files", padx=5, pady=5, command=declutter)
declutter_button.pack()

window.mainloop()
