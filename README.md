# PythonKeyLog
Ben Woodfield - Raser Apps
Python Key Logging program

Dependencies:
* Linux System
* Python 2.7 (not tested on 3)
* Python Module: python-xlib

python-xlib installation:
If I remember rightly, I tried the pip installation (pip install xlib) and had no luck, I ended up using the apt-get method(sudo apt-get install python-xlib). You may have to try these and if not look up how to install Xlib for your version of Python online.

Usage:
Before testing 

Open KeyLog.py and go to LINE 12.
Change the file-path or location of 'outputfile.log' to the file path you want to save it to on YOUR system. Otherwise it won't save.
eg: if you want the keylog output to save to a file on the desktop, change the filepath to your desktop (/home/user/Desktop/outputfile.log or whatever it is on your system).

Now you are ready to deploy.

Test Done: 
This works fine on Linux systems (Ubuntu, Raspbian, Kali)

I tried to deploy via SSH and had display errors relating to x environment. Needs work for this purpose.

To Do:
* Get running in SSH environment
* Add user input (choice of filename and destination)
* Maybe make this more visually pleasing (Tkinter would be my choice otherwise this would only add more dependencies)

Let me know what you think. feel free to add or improve, andmake any suggestions. I am still learning.

raserppsprograms@gmail.com
