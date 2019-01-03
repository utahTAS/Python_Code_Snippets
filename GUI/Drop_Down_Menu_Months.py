####################################################################
##Create a dropdown menu with months for the user to choose from.  ##
#####################################################################

from tkinter import Tk
from tkinter import *

master = Tk()
master.attributes("-topmost", True)      #makes the dialog appear on top

#create the variable to hold the dropdown value
variable1 = StringVar(master)

#set dropdown default value
variable1.set("January") 

#create dropdown. Each text item is an entry in the dropdown. Positional variable
#1 gives the tk window to use, and pos 2 give the variable to hold dropdown value
w = OptionMenu(master, variable1, 'January','February', 'March','April', 'May',
               'June', 'July', 'August', 'September', 'October', 'November', 'December')
w.grid(row=1, sticky=W, column=0)

#when the user presses okay get the final value of the drpodown
def quit():
    global choice
    #this is the variable we wanted from the user
    choice=variable1.get()
    master.destroy()

#it's best to have the code wait for the user to press okay to move on. 
#This prevents having to check if the state of the window has changed.
button = Button(master, text="OK", command=quit)
button.grid(row=5, sticky=W, column=2)

#final variable we wanted to keep here is 'choice'


mainloop()
