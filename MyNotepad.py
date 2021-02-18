from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None
    TextArea.delete(1.0,END)

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file=="":
            file=None
        else:
            #Save as a newfile
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+" - Notepad ")
            print("File Saved")
    else:
            #Save as a newfile
            f=open(file,'w')
            f.write(TextArea.get(1.0,END))
            f.close()



def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))
    
def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    

def about():
    showinfo("MyNotepad","Notepad created by Darshan Agrawal ")


if __name__=='__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("MYNotepad-Notepad")
    root.wm_iconbitmap("G:\python development\Python GUI Development\MyNotepad\A1.ico")
    root.geometry("644x788")
    
    #Add TextArea
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)

    #Create a MenuBar
    MenuBar=Menu(root)
    
    #filemenu starts
    FileMenu=Menu(MenuBar,tearoff=0)
    
    #Open new file
    FileMenu.add_command(label="New",command=newFile)

    #Open Existing File
    FileMenu.add_command(label="Open",command=openFile)

    #Save current file
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=FileMenu)
    #File menu Ends

    #Edit menu starts
    EditMenu=Menu(MenuBar,tearoff=0)
    
    #to give a feature of cut copy and  paste
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)

    MenuBar.add_cascade(label="Edit",menu=EditMenu)

    #Edit Menu Ends

    #Help Menu Starts

    HelpMenu=Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=HelpMenu)


    #Help Menu Ends

    #Adding Scrollbar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    root.config(menu=MenuBar)

    root.mainloop()

