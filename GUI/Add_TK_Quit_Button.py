###########################################################
## Create a tk window that has a close button label "OK" ##
###########################################################


from tkinter import Tk
from tkinter import *

#start the tk window, make it always on top
master = Tk()
master.attributes("-topmost", True)      #makes the dialog appear on top

#function to close the window when the button is pressed
def quit():
    master.destroy()

#Create the button. The button text is specified by the text arg. 
#This one will say "OK"
button = Button(master, text="OK", command=quit)


#define button location. In this case the buttons location is definted in a grid.
#The 'sticky=W' gives right aligned features. Case use any of 'NSEW'.
button.grid(row=10, column=2, sticky=W,)
