import tkinter
from tkinter import Text
class Caesar_Cipher: 
    def __init__(self,frame):
        self.root=frame
        self.frame=tkinter.Frame(self.root,width=600,height=200,relief="ridge",bg="#000000",bd=10)
        self.encrypt=tkinter.Entry(self.frame,font=("Courier",16))
        self.key=tkinter.Entry(self.frame,font=("Courier",16))
        self.lencrypt=tkinter.Label(self.frame,text="Encrypted text:",justify="left",anchor="w", bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decrypted text:",justify="left",anchor="w", bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.lkey=tkinter.Label(self.frame,text="Key:",justify="left",anchor="w",bg="#000000", fg="#FFFFFF",font=("Courier",16))
        self.execute=tkinter.Button(master=self.frame,text="decrypt",fg="#FFFFFF",bg="#000000",bd=4,font=("Courier",16),width=600,height=20,command=self.decrypt) 
        self.quit=tkinter.Button(self.frame,text="X",activebackground="#FF0000",fg="#FFFFFF",bg="#000000",bd=1,width=20,height=20,command=self.frame.place_forget)
    def build(self):
        self.lencrypt.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.encrypt.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.lkey.place(x=0,y=50,anchor="nw",width=200,height=20)
        self.key.place(x=201,y=50,anchor="nw",width=330,height=20)
        self.ldecrypt.place(x=0,y=90,anchor="nw",width=580,height=20)
        self.execute.place(x=0,y=130,anchor="nw",width=580,height=50)
        self.quit.place(x=560,y=0,anchor="nw",width=20,height=20)
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


