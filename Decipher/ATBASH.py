import tkinter
class Atbash_Cipher:
    def __init__(self,frame):
        self.root=frame
        self.frame=tkinter.Frame(master=self.root,width=600,height=200,relief="ridge",bg="#000000",bd=10)
        self.lencrypt=tkinter.Label(self.frame,text="Encrypted text:",justify="left",anchor="w",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decrypted text:",justify="left",anchor="w",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.encrypt=tkinter.Entry(self.frame,font=("Courier",16))
        self.execute=tkinter.Button(self.frame,text="decrypt",command=self.decrypt,bg="#000000",fg='#FFFFFF',bd=4)
        self.quit=tkinter.Button(self.frame,text="X",activebackground="#FF0000",fg="#FFFFFF",bg="#000000",bd=1,width=20,height=20,command=self.frame.place_forget)

    def build(self):
        self.lencrypt.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.ldecrypt.place(x=0,y=50,anchor="nw",width=580,height=20)
        self.encrypt.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.execute.place(x=201,y=130,anchor="nw",width=580,height=20)
        self.quit.place(x=560,y=0,anchor="nw",width=20,height=20)
        self.frame.place(x=0,y=0,anchor="nw")

    def decrypt(self):
        tmp=[]
        result=str
        for c in self.encrypt.get():
            c=ord(c)
            while c<65:
                c+=26
            while c>122:
                c-=26
            if c>=65 and c<=90:
                c=(90-c)+65
            elif c>=96 and c<=122:
                c=(122-c)+97
            tmp.append(chr(c))
        result="-".join(tmp)
        self.ldecrypt.configure(text="Decrpted text: "+result)