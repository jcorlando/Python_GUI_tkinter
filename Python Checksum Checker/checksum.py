#!/usr/bin/python3
from tkinter import *

window = Tk()                                       # Create root node
window.title('Python file Checksum Hash Checker')

# setting the minimum size of the root window
window.minsize(540, 200)

window.geometry("600x350")    # Set intial height and width of window

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


window.columnconfigure(0, weight=1)                                         # Configure Columns
window.rowconfigure([0, 1], weight=1)                                       # Configure Rows
title = Label(window, text="Checksum Checker", fg="white", bg="black")      # Create the Title Label widget
title.grid(row=0, column=0, sticky="new")                                   # "new" means "north", "east", "west"



labelButton = Label(window, text="Choose a file to Checksum:")
labelButton.grid(row=1, column=0, sticky="w", padx=15)

button1 = Button(window, text ="Choose filepath")
button1.grid(row=1, column=0, sticky="w", padx=200)



window.config(menu=menubar)
window.mainloop()
