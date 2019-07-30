import tkinter

class A1Z26_Cipher:
    def __init__(self,root):
        self.root=root
        self.frame=tkinter.Frame(master=self.root,width=600,height=200,relief="sunken",bg="#000000",bd=10)
        self.lencrypt=tkinter.Label(self.frame, text="Encrypted text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decryped text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.eencrypt=tkinter.Entry(self.frame, font=("Courier",16),bd=2)
        self.execute=tkinter.Button(self.frame,text="decypt",bg="#000000",fg='#FFFFFF',bd=4,command=self.decrypt)

    def build(self):
        self.lencrypt.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.ldecrypt.place(x=0,y=50,anchor="nw",width=580,height=20)
        self.eencrypt.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.execute.place(x=0,y=130,anchor="nw",width=580,height=50)
        self.frame.place(x=0,y=0,anchor="nw")
    
    def decrypt(self):
        result=""
        tmp=""
        code=self.eencrypt.get()
        for c in code:
            if c!=" " and c!="-":
                tmp+=c
            if c=="-" or c==" ":
                try:
                    result+=chr(64+int(tmp))
                    if c==" ":
                        result+=" "
                    tmp=""
                except:
                   self.ldecrypt.configure(text="Error: check that you input only numbers",bg="red")
                   break
        try:
            result+=chr(64+int(tmp))
        except:
            pass
        self.ldecrypt.configure(text="Decrypted text: "+result)

