#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog

window = Tk()                                       # Create root node
window.title('File Checksum Hash Checker')

# setting the minimum size of the root window
window.minsize(630, 200)

window.geometry("650x350")    # Set intial height and width of window

#----------Add a menubar with exit command--------------
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)
#----------Add a menubar with exit command--------------

#----------Add a menubar with about command-----------------
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...")
menubar.add_cascade(label="Help", menu=helpmenu)
#----------Add a menubar with about command-----------------


window.columnconfigure(0, weight=1)                                         # Configure Column 0
title = Label(window, text="Checksum Checker", fg="white", bg="black")      # Create the Title Label widget
title.grid(row=0, column=0, sticky="new")                                   # "new" means "north", "east", "west"


labelButton = Label(window, text="Choose a file to find its Checksum:")
labelButton.grid(row=1, column=0, sticky="nw", padx=10)

#------------Define a Function to save the filepath--------------
def filepathname():
    window.filename = filedialog.askopenfilename(title="Choose a File")
#------------Define a Function to save the filepath--------------

button1 = Button(window, text ="Choose filepath", command=filepathname)
button1.grid(row=1, column=0, sticky="nw", padx=250)


window.rowconfigure(2, weight=1)                                            # Configure Row 2
label_file_path = Label(window, text="The Path to your file is :")
label_file_path.grid(row=2, column=0, sticky="nw", padx=10)



window.config(menu=menubar)
window.mainloop()
