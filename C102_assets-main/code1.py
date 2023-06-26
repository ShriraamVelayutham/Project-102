import os
import shutil

from_dir = "destination"
to_dir = "images"

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name , extension = os.path.splitext(file_name)

    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path_1 = from_dir+ '/' +file_name
        path_2 = to_dir + '/' + "Document_Files"
        path_3 = to_dir + '/' + "Document_Files" + '/' + file_name
        if os.path.exists(path_2):
            print("Moving " +  file_name + ".....")
            shutil.move(path_1,path_3)
        else:
            print("Creating the image folder")
            os.makedirs(path_2)
            print("Moving " +  file_name + ".....")
            shutil.move(path_1,path_3)

