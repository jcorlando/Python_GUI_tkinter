#!/usr/bin/python3
from tkinter import *

window = Tk()                                                    # Create root node
window.geometry("500x350")                                          # Set intial height and width of window
window.columnconfigure(0, weight=1)                                 # Configure First Column
window.rowconfigure(0, weight=1)                                    # Configure First Row
title = Label(window, text="Checksum Checker", fg="white", bg="black")   # Create the Title Label widget
title.grid(row=0, column=0, sticky="new")                           # "new" means "north", "east", "west"




window.mainloop()
