import os 
cwd =os.getcwd();
# print("Current working dir is :",cwd);
#change working dir
# def current_path():
#     print("Current working dir before");
#     print(os.getcwd());
#     print();
      
# current_path();

# os.chdir('../');

# current_path();

# directory="test";
# parent_dir="Z:\python";
# path=os.path.join(parent_dir,directory);
# print(path);
# os.mkdir(path);
# print("Directory '%s' created" %directory)

#second directory with permision

# directory="test2";
# parent_dir="Z:\python";
# mode=0o666;
# path=os.path.join(parent_dir,directory)
# os.mkdir(path,mode)
# print("Directory '%s' created" %directory)

# third directory with sub directory
# directory="test3";
# parent_dir="Z:\python";
# path=os.path.join(parent_dir,directory);
# os.makedirs(path);
# print("Directory '%s' created"%directory);


#list directory
# path="/";
# list_dir=os.listdir(path);
# print("Files and directories in '", path, "' :");
# print(list_dir);

#delete file
# file="file2.txt";
# location="Z:\python";
# path=os.path.join(location,file);
# os.remove(path);
# os.remove("Z:\python\test1.txt")

# delete directory
# directory="test3";
# path="Z:\python";
# path2=os.path.join(path,directory);
# os.rmdir(path2);

# comman use function
# print(os.name);

#open file error
# try:
#     filename='GFG.txt';
#     f=open(filename,'rU')
#     text=f.read();
#     print(text);
#     f.close();
# except IOError:
#     print("Problem reading :" + filename)
    
#os.popen

# file=open('GFG.txt','w');
# file.write("hello");
# file.close();

# file=open('GFG.txt','r');
# text=file.read();
# print(text);

# file=os.popen('GFG.txt','w');
# file.write("hello");

#os.close
# fd="GFG.txt"
# file=open(fd,'r')
# text=file.read()
# print(text)
# file.close()

#os.rename()
# fd="GFG.txt"
# os.rename(fd,"GFF.txt")

#os.remove()
#os.remove("GFF.txt")

#os.path.exists()
# result=os.path.exists("GFF.txt")
# print(result)

#os.path.getsize()
# size=os.path.getsize("GFF.txt")
# print(size)#sow output in bytes

#pickle
#dump in file
import pickle as pk
# data={'name':'ashish','age':30,'name:akash':'akash','age':12}
# with open('data.pk','wb') as file:
#     pk.dump(data,file)

#read from file 
# with open('data.pk',"rb") as file:
#     loaded_data=pk.load(file)
# print(loaded_data)

# obj1={'name':'google','emp_name':"ashish g patni"}
# obj2={"name":"oracle","emp_name":"akash"}
# with open("data2.pk","wb") as file :
#     pk.dump(obj1,file)
# with open("data2.pk","wb") as file:
#     pk.dump(obj2,file)
# with open("data2.pk","rb") as file:
#     data=pk.load(file)
    
# print(data);

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
# person1=person("Charlie",40)
# with open("person.pk","wb") as file:
#     pk.dump(person1,file,protocol=4)
            
# with open("person.pk","rb") as file:
#     person2=pk.load(file)
# print(person2.name);

# try:
#     with open("data2.pk","rb") as file:
#         data=pk.load(file)
#         print(data)
# except FileNotFoundError:
#     print("File not found")
# except pk.UnpicklingError:
#     print("Error")


import pickle

# Simulate loading data from untrusted source
malicious_data = b'\x80\x04\x95\x1b\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x08'

try:
    loaded_data = pickle.loads(malicious_data)
except pickle.UnpicklingError:
    print("Error while unpickling malicious data!")
