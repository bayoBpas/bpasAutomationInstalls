#add a condition that cuts out the graph if revit is open. or give the user the option to close the application.###############

#import the required libraries
import os
import shutil
import time
import tkinter as tk
import psutil

#check if the source directory of the BPAS pyRevit extension is accessible. Quit if not
if not os.path.exists(r'Z:\IT\Dynamo Packages\bpasLogo.gif') or not os.path.exists( r'Z:\IT\Dynamo Packages\2.13') :quit()

#check if revit is running. Quit if running.
if ("Revit.exe" in (p.name() for p in psutil.process_iter()) or "revit.exe" 
in (p.name() for p in psutil.process_iter())) :quit()


##################create splash screen##############################
#Create the root window
root = tk.Tk()

#Set the dimensions of the splash screen
root.geometry("400x400")

#Hide the window's frame and controls
root.overrideredirect(True)

# Set the title of the splash screen
root.title("Dynamo Package Install")

root.eval('tk::PlaceWindow . center')

#Create a label to hold the notification text
label = tk.Label(root, text="Dynamo packages are installing. Please wait and leave this window open.",
                 justify=tk.RIGHT)

#Create a label to hold the background image
image = tk.Label(root)

#Set the image of the label
image.image = tk.PhotoImage(file=r"Z:\IT\Dynamo Packages\bpasLogo.gif")
image.config(image=image.image)


#Function to animate the gif
def animate():
    try:
        # Update the image of the label
        image.image = tk.PhotoImage(file="bpasLogo.gif")
        image.config(image=image.image)
    except:
        pass
    finally:
        # Call this function again to animate the gif
        image.after(1000, animate)

root.after(0, animate)

# Pack all the widgets
label.pack()
image.pack()



################## install packages##################
def runPackageCode():
    #get current username in session
    userName = os.getlogin()
    print(userName)

    #target directory for the dynamo packages.Combine username with directory path beginning and end for target directory
    begDir = r'C:/Users/'
    endDir = 'AppData/Roaming/Dynamo/Dynamo Revit/2.13'
    target_dir = os.path.join(begDir,userName,endDir)
    print(target_dir)


    # Source directory for the dynamo packages on the server
    source_dir = r'Z:\IT\Dynamo Packages\2.13'


    #get all file names in the source directory
    fileNames = os.listdir(source_dir)
    print(fileNames)


    # Check if the target directory exists
    if not os.path.exists(target_dir):
        # Copy the dynamo package folder if the folder does not exist at the target path
        shutil.copytree(source_dir, target_dir)


    #check if the source directory has been modified more recently than the target directory
    print(os.path.exists(source_dir) and os.path.getmtime(source_dir) > os.path.getmtime(target_dir))
    if os.path.exists(source_dir) and os.path.getmtime(source_dir) > os.path.getmtime(target_dir):

        #delete target directory if it exists
        if os.path.exists(target_dir):
            # Delete file
            if os.path.isfile(target_dir):
                os.remove(target_dir)
            # Delete directory
            else:
                shutil.rmtree(target_dir)

        shutil.copytree(source_dir, target_dir)

        #close the splash screen
        root.destroy()

    else:
        quit()

#schedule package copying code to run after 1000 milliseconds
root.after(1000,runPackageCode)

# Start the main event loop
root.mainloop()
