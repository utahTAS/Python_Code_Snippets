#############################################################
## Use tkinter to get a string with the path to a specific ## 
## file.                                                    ##
#############################################################

from tkinter.filedialog import askopenfilename
from tkinter import *

def get_dat():
    root = Tk()
    root.withdraw()
    root.focus_force()
    root.attributes("-topmost", True)      #makes the dialog appear on top
    filename = askopenfilename()      # Open single file
    
    return filename

filename=get_dat()
