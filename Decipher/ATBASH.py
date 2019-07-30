import tkinter
class Atbash_Cipher:
    def __init__(self,frame):
        self.root=frame
        self.frame=tkinter.Frame(master=self.root,width=790,height=750,relief="sunken",bg="#000000",bd=10)
        self.lencrypt=tkinter.Label(self.frame,text="Encrypted text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decrypted text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.encrypt=tkinter.Entry(self.frame,font=("Courier",16))
        self.bdecrypt=tkinter.Button(self.frame,text="decrypt",command=self.decrypt,bg="#000000",fg='#FFFFFF',bd=4)

    def build(self):
        self.lencrypt.grid(row=0,column=0,sticky="w")
        self.ldecrypt.grid(row=2,column=0,sticky="w")
        self.encrypt.grid(row=0,column=1,columnspan=2)
        self.bdecrypt.grid(row=3,column=0,sticky="w")
        self.frame.grid()

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