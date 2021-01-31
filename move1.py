import os, shutil

# current folder which consists of all the files that user wants to move
CURRENT = r'C:\Users\Asus\Documents\PYTHON\projects\moveInOut\currentFolderTest'

# folders to move specific files into
MP4 = r'C:\Users\Asus\Documents\PYTHON\projects\moveInOut\mainFolderTest\MP4 ONLY'
WORD = r'C:\Users\Asus\Documents\PYTHON\projects\moveInOut\mainFolderTest\WORD ONLY'
JPEG = r'C:\Users\Asus\Documents\PYTHON\projects\moveInOut\mainFolderTest\JPEG ONLY'
ZIP = r'C:\Users\Asus\Documents\PYTHON\projects\moveInOut\mainFolderTest\ZIP ONLY'


for root, subdirs, files in os.walk(CURRENT):
    for file in files:
        if file.endswith(('.mp4')):
            path = os.path.join(root, file)
            shutil.move(path, MP4)
        elif file.endswith(('.zip')):
            path = os.path.join(root, file)
            shutil.move(path, ZIP)
        elif file.endswith(('.docx')):
            path = os.path.join(root, file)
            shutil.move(path, WORD)
        elif file.endswith(('.jpeg')):
            path = os.path.join(root, file)
            shutil.move(path, JPEG)
        else:
            print('No files')
