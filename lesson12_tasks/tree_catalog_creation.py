import os
import sys
from pathlib import Path

foldersList = ['Folder1', 'Folder2', 'Folder3', 'Folder4']
# ---- if "Mainfolder" is not exists - create this folder
def main_folder_creation (currentFolder, mainfolder):
    subfoldersList = ['Subfolder1', 'Subfolder2', 'Subfolder3', 'Subfolder4']
    filesList = ['File_01.txt', 'File_02.txt', 'File_03.txt', 'File_04.txt']
    if not os.path.isdir(currentFolder+"\\"+mainfolder):
        os.mkdir(mainfolder)
        print("Directory %s was created." %mainfolder)
        # ---- get current folder
        currentFolder = os.getcwd()
        # ---- name of template main folder
        mainfolder = "Mainfolder"
        # --- go to Mainfolder
        os.chdir(currentFolder+"\\"+mainfolder)
        folder = os.getcwd()
        # ---- create a template tree
        def item_creation(itemlist, mainfolderPath):
            counter=0
            for item in itemlist:
                path = mainfolderPath + "\\" + item
                os.mkdir(path)
                os.chdir(path)
                os.makedirs(os.getcwd()+"\\"+subfoldersList[counter])
                file = open(os.getcwd() + "\\" + filesList[counter], 'w')
                file.close()
                counter+=1
    else:
        print('Directory exists')
        #sys.exit(0)
# ---- call a function for tree creation
#item_creation(foldersList, folder)







