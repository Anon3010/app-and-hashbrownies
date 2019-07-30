import tkinter

class A1Z26_Cipher:
    def __init__(self,root):
        self.root=root
        self.frame=tkinter.Frame(master=self.root,width=790,height=750,relief="sunken",bg="#000000",bd=10)
        self.lencrypt=tkinter.Label(self.frame, text="Encrypted text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.ldecrypt=tkinter.Label(self.frame,text="Decryped text:",justify="left",bg="#000000",fg='#FFFFFF',font=("Courier",16))
        self.eencrypt=tkinter.Entry(self.frame, font=("Courier",16),bd=2)
        self.execute=tkinter.Button(self.frame,text="decypt",bg="#000000",fg='#FFFFFF',bd=4,command=self.decrypt)

    def build(self):
        self.lencrypt.grid(row=0,column=0,sticky="w")
        self.ldecrypt.grid(row=1,column=0,sticky="w",padx=10)
        self.eencrypt.grid(row=0,column=1,columnspan=2,sticky="w")
        self.execute.grid(row=2,column=0,sticky="w")
        self.frame.grid()
    
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

