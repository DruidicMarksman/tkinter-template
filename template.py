import tkinter
from tkinter import * # importing all modules

root = Tk() # initializing Tkinter window

root.title("The name of the GUI window") 

root.geometry("500x500") # width and height in pixels

btn = Button(root, text="button text", command = root.destroy) # GUI button which closes the window when clicked

btn.pack(side=BOTTOM) # loads the button in the GUI

root.mainloop() # opens the GUI window

