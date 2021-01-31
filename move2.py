import os, shutil

# current path for the folder that consists of files to be moved
CURRENT = input('Current destination of the files to move :\n')

# path of the folder where the files will be moved into
PATH_1 = input('New destination for the files :\n')

# user inputs the extension of files needed to move
EXTENSION = input('Please choose the desired extension of files needed to be moved\nChoose from: [.mp3, .mp4, .jpeg, .zip, .docx] or "a" for all :\n').lower()


checkAndMove = True

while checkAndMove:
    for root, subdirs, files in os.walk(CURRENT):
        if EXTENSION != 'a':
            for file in files:
                if file.endswith((EXTENSION)):
                    path = os.path.join(root, file)
                    shutil.move(path, PATH_1)
        elif EXTENSION == 'a':
            for file in files:
                    path = os.path.join(root, file)
                    shutil.move(path, PATH_1)  

    
