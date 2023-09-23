import os
import glob
# sow os
# print(os.name)

#SOW ALL SYSTEM INFO
# print(os.uname())

#Make folder 
# os.makedirs("make_folder");

#folder path
# print(os.walk("make_folder"))

# current folder
cur_folder=os.getcwd()
getpath="E:\python\python_pickel_os"
# root folder,sub folder,file

# for root_folder,sub_folder,file in os.walk(getpath):
#     print(file)

# change directory
# os.chdir("E:\oosp")

#filelist
# first method
# folder_path="E:\\oosp"
# file_list=os.listdir(folder_path)
# print(file_list[3])


# second method (find path)
file_list= glob.glob(os.path.join(os.getcwd(),"*"))
print(file_list[1])