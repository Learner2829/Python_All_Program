from tkinter import *
# from PIL import image, ImageTk``
root=Tk()

# set hight widhth
root.geometry("800x400")

#minsize
root.minsize(800,400)

# maxsize
# root.maxsize(800,434)

# lable
# lb=Label(text="Hello This is ashish window")
# lb.pack()

# add image in window 
# photo=PhotoImage(file="png-transparent-spider-man-heroes-download-with-transparent-background-free-thumbnail.png")
# img=Label(image=photo)
# img.pack()

#title
root.title("My first window"); 

# importent lable
# text-adds the text
# bd-background
# font- sets the font
# padx 
# pady
# relief

# title_lable =Label (text=''' On Windows:
# Open the Control Panel and search for "Environment Variables."
# Click on "Edit the system environment variables."
# In the System Properties window, click the "Environment Variables" button.
# Under "System variables," find the "Path" variable, and click "Edit."
# Click "New" and add the path to your Python installation directory, which typically looks like C:\PythonXX (replace XX with your version, like 3.9).
# Click "OK" to close the windows.''' ,bg="black",foreground="green",padx=20,pady=20,font=("comicsansms",15,"bold"),borderwidth=5,relief=SUNKEN)
# title_lable.pack(); 

#test lable
# Pack option

# lb1.pack()
# title_lable.pack(anchor="ne")
# lb1.pack(anchor="sw")
# lb1.pack(side=BOTTOM,anchor="sw")



# Add border and side
f1=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT,fill="y")
lb1=Label(f1,text="Wellcome to my project",bg="yellow")
lb1.pack(anchor="nw",fill=X)

# second frem
f2=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill=X)
lb2=Label(f2,text="This is second",bg="yellow")
lb2.pack()

def hello():
    for x in range(1,5):
        print(x)
    
# Add button
f3=Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
f3.pack(side=LEFT,anchor="nw")
b1=Button(f3,text="Print",command=hello)
b1.pack()



#main Display
root.mainloop() 


