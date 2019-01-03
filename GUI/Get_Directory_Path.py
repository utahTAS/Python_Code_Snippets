#########################################################################################
## Use this code to open a file dialog that gets the name of a directory that the user ##
## chooses. The directory name is saved as a string in the variable outfile_path  in   ##
## example. Requires the instal of wx python. https://anaconda.org/anaconda/wxpython   ##
#########################################################################################

import wx

app = wx.App()
 
frame = wx.Frame(None, -1, 'win.py')
frame.SetDimensions(0,0,200,50)
 
# Create open file dialog
openFileDialog = wx.DirDialog(frame, "Choose folder to save output to", "",
            wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)
 
openFileDialog.ShowModal()
print(openFileDialog.GetPath())

# outfile_path is the string with the path name saved as a variable
outfile_path = openFileDialog.GetPath()+'\\'
openFileDialog.Destroy()

del app


