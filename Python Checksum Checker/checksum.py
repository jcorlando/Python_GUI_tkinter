#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog


window = Tk()                                       # Create root node
window.title('File Checksum Hash Checker')

# setting the minimum size of the root window
window.minsize(850, 290)

# Set intial height and width of window
window.geometry("850x290")

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

#------------Define a Function For When Button is clicked and filepath is saved--------------
filepath = StringVar()
filepath.set("")
md5_sum = StringVar()
md5_sum.set("")
md5_sum.set("Hello World!")
sha1_sum = StringVar()
sha1_sum.set("")
sha1_sum.set("Hello World!")
sha256_sum = StringVar()
sha256_sum.set("")
sha256_sum.set("Hello World!")
def openFile():
    filepath.set(filedialog.askopenfilename(title="Choose a File"))
    label_path = Label(window, textvariable=filepath)
    label_path.grid(row=2, column=0, sticky="nw", padx=180)
    filepath_string = filepath.get()
    label_md5_sum = Label(window, textvariable=md5_sum)
    label_md5_sum.grid(row=3, column=0, sticky="nw", pady=20, padx=180)
    label_sha1_sum = Label(window, textvariable=sha1_sum)
    label_sha1_sum.grid(row=4, column=0, sticky="nw", pady=20, padx=180)
    label_sha256_sum = Label(window, textvariable=sha256_sum)
    label_sha256_sum.grid(row=5, column=0, sticky="nw", pady=20, padx=180)
#------------Define a Function For When Button is clicked and filepath is saved--------------

button1 = Button(window, text ="Choose filepath", command=openFile)
button1.grid(row=1, column=0, sticky="nw", padx=250)


label_file_path = Label(window, text="The Path to your file is :")
label_file_path.grid(row=2, column=0, sticky="nw", padx=10)


label_MD5_Sum = Label(window, text="The MD5 Sum is :")
label_MD5_Sum.grid(row=3, column=0, sticky="nw", pady=20, padx=10)


label_MD5_Sum = Label(window, text="The SHA1 Sum is :")
label_MD5_Sum.grid(row=4, column=0, sticky="nw", pady=20, padx=10)


window.rowconfigure(5, weight=1)                          # Configure Row 5
label_MD5_Sum = Label(window, text="The SHA256 Sum is :")
label_MD5_Sum.grid(row=5, column=0, sticky="nw", pady=20, padx=10)


window.config(menu=menubar)
window.mainloop()
