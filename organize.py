import os
import shutil
from_dir="C:/Users/Trisha/Downloads"
to_dir="C:/Users/Trisha/OneDrive/Desktop/imagesC102"
list_of_files=os.listdir(from_dir)
#print(list_of_files)
for i in list_of_files:
    name,extension=os.path.splitext(i)
    if extension== " ":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1=from_dir+'/'+i
        path2=to_dir+'/'+"image_files"
        path3=to_dir+'/'+"image_files"+'/'+i
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving"+i+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+i+"...")
            shutil.move(path1,path3)