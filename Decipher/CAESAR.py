import tkinter
from tkinter import Textfield
class Caesar_Cipher: 
    def __init__(self,frame):
        self.root=frame
        self.frame=tkinter.Frame(self.root,width=800,height=200,relief="sunken",bg="#000000",bd=10)
        self.encrypt=tkinter.Entry(self.frame,font=("Courier",16))
        self.key=tkinter.Entry(self.frame,font=("Courier",16))
        self.lencrypt=tkinter.Label(self.frame,text="Encrypted text:",justify="left", bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decrypted text:",justify="left", bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.lkey=tkinter.Label(self.frame,text="Key:",justify="left", bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.execute=tkinter.Button(master=self.frame,text="decrypt",fg="#FFFFFF",bg="#000000",bd=4, command=self.decrypt) 
        self.properties=tkinter.Textfield

    def build(self):
        self.lencrypt.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.encrypt.place(x=201,y=10,anchor="nw",width=500,height=20)
        self.lkey.place(x=0,y=30,anchor="nw",width=200,height=20)
        self.key.place(x=201,y=30,anchor="nw")
        self.ldecrypt.place()
        self.execute.place()
        self.frame.place(x=0,y=0,anchor="nw")
    def decrypt(self): #Alphabet version
        result=str
        lt=[]
        try:
            val=int(self.key.get())
        except:
            self.ldecrypt.configure(text="Error: please check that your key is a number")
        for c in self.encrypt.get().upper():
            if c==" ":
                lt.append(" ")
                continue
            tmp=ord(c)+val
            while tmp<65:
                tmp+=26
            while tmp>90:
                tmp-=26
            lt.append(chr(tmp))
        result="".join(lt)
        self.ldecrypt.configure(text="Decrypted text: "+result)
    

