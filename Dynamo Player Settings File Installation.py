import os
import shutil
import time

#check if the source directory is accessible. Quit if not
if not os.path.exists(r'Z:`\IT\Dynamo Player Settings\dynamoplayer-5'):quit()

#get current username in session
userName = os.getlogin()
print(userName)

# Target directory for the dynamo player settings.Combine username with directory path beginning and end
begDir = r'C:/Users/'
endDir = 'AppData\Local\dynamoplayer-5'
target_dir = os.path.join(begDir,userName,endDir)
print(target_dir)


# Source directory for the dynamo player settings on the server
source_dir = r'Z:\IT\Dynamo Player Settings\dynamoplayer-5'


#get all names files in the source directory
fileNames = os.listdir(source_dir)
print(fileNames)


# Check if the target directory exists
if not os.path.exists(target_dir):
    # Copy the dynamo player settings folder if the folder does not exist at the target path
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
    quit()
