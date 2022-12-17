#import the required libraries
import os
import shutil
import time
import configparser
import sys

#check if the source directory of the BPAS pyRevit extension is accessible. Quit if not
if not os.path.exists(r'Z:\CAD Projects\B - BIM TEMPLATES\I - PYREVIT\bpas'):quit()

###############download BPAS extension file to computer###############

#get current username in session
userName = os.getlogin()
print(userName)

#target directory for the bpas extensions folder. Combine username with directory path beginning and end
begDir = r'C:/Users/'
endDir = 'AppData/Roaming/pyRevit/bpas'
target_dir = os.path.join(begDir,userName,endDir)
print(target_dir)


# Source directory for the bpas pyRevit extension folder on the server
source_dir = r'Z:\CAD Projects\B - BIM TEMPLATES\I - PYREVIT\bpas'


#get all file names in the source directory
fileNames = os.listdir(source_dir)
print(fileNames)


# Check if the target directory exists
if not os.path.exists(target_dir):
    # Copy the bpas extension folder if the folder does not exist at the target path
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

else:
    sys.exit()

#################pyRevit settings and config file update##################

#open the pyRevit configuration files from the current users computer
conBegDir = r'C:/Users/'
conEndDir = 'AppData\Roaming\pyRevit\pyRevit_config.ini'
configPath = os.path.join(conBegDir,userName,conEndDir)

#check if the bpas extension file has been updated more recently than the config file
print(os.path.exists(target_dir) and os.path.getmtime(target_dir) > os.path.getmtime(configPath))
if os.path.getmtime(target_dir) > os.path.getmtime(configPath):

    #modify the config file if the bpas extension file has been modified more recently than the config file

    #read the current contents of the config file
    config = configparser.ConfigParser()
    config.read(configPath)

    #create text to be written to config files
    configText = '["'+target_dir+'"]'
    print(configText)

    #get the contents of the pyRevit config file at the core in userextensions
    print((config.get("core", "userextensions")))

    #write the new contents to the config file
    config.set("core", "userextensions", configText)
    with open(configPath, "w") as config_file:
        config.write(config_file)
