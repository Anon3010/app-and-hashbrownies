import tkinter 
#from Controller import Controller

class Cipher:
    # Classe von dem später alle dcoder abgeleitet werden sollen
    # Die Frage die sich jetzt alle stellen: Warum macht der typ sich die mühe
    # und gestaltet das Programm so objektorientiert?
    # Ganz einfach: Weil ich es ausprobieren wollte!
    
    def __init__(self,master,language):
        self.frame=tkinter.Frame(master=master,width=600,height=200,relief="ridge",bg="#262626",bd=10)
        self.lencrypted=tkinter.Label(self.frame,anchor="w",justify="left",bg="#262626",fg="#FFFFFF",font=("Courier",16),text="Encoded text:")#Controller.language[Controller.cur_language]["lencrypt"])
        self.ldecrypted=tkinter.Label(self.frame,anchor="w",justify="left",bg="#262626",fg="#FFFFFF",font=("Courier",16),text="Decoded text:")#Controller.language[Controller.cur_language]["ldecrypt"])
        self.encrypted=tkinter.Entry(self.frame,font=("Courier",16), bg="#262626", fg="#FFFFFF")
        self.decrypted=tkinter.Entry(self.frame,font=("Courier",16), bg="#262626", fg="#FFFFFF")
        self.execute=tkinter.Button(self.frame,bg="#262626",fg="#FFFFFF",font=("Courier",16),bd=4,text="decrypt",command=self.decrypt)
        self.quit=tkinter.Button(self.frame,bg="#262626",fg="#FFFFFF",font=("Courier",16),width=20,height=20,text="X",command=self.frame.place_forget)
        
    def build(self):
        self.frame.place(x=0,y=0,anchor="nw")
        self.lencrypted.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.ldecrypted.place(x=0,y=50,anchor="nw",width=200,height=20)
        self.encrypted.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.decrypted.place(x=201,y=50,anchor="nw",width=330,height=20)
        self.execute.place(x=0,y=130,anchor="nw",width=580,height=50)
        self.quit.place(x=560,y=0,anchor="nw",width=20,height=20)
    
    def decrypt(self):
        pass




class Caesar_Cipher(Cipher):

    def __init__(self,master,language):
        Cipher.__init__(self,master,language)
        self.lkey=tkinter.Label(self.frame,anchor="w",bg="#262626",fg="#FFFFFF",font=("Courier",16),text="Key")#language[Controller.cur_language]["lkey"])
        self.key=tkinter.Entry(self.frame,font=("Courier",16), bg="#262626", fg="#FFFFFF")
    
    def build(self):
        self.frame.place(x=0,y=0,anchor="nw")
        self.lencrypted.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.ldecrypted.place(x=0,y=90,anchor="nw",width=200,height=20)
        self.encrypted.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.decrypted.place(x=201,y=90,anchor="nw",width=330,height=20)
        self.execute.place(x=0,y=130,anchor="nw",width=580,height=50)
        self.quit.place(x=560,y=0,anchor="nw",width=20,height=20)
        self.lkey.place(x=0,y=50,anchor="nw",width=200,height=20)
        self.key.place(x=201,y=50,anchor="nw",width=330,height=20)
    
    def decrypt(self):
        result=""
        lt=[]
        try:
            val=int(self.key.get())
        except:
            pass
        for c in self.encrypted.get().upper():
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
        self.decrypted.delete(0,"end")
        self.decrypted.insert(0,result)
        

class Atbash_Cipher(Cipher):

    def __init__(self,master,language):
        Cipher.__init__(self,master,language)
    
    def build(self):
        Cipher.build(self) 
    
    def decrypt(self):
        result=""
        for c in self.encrypted.get().upper():
            if c==" ":
                result+=c
            else:
                c=ord(c)
                result=result+chr(90-(c-65))
        self.decrypted.delete(0,"end")
        self.decrypted.insert(0,result)

class A1Z26_Cipher(Cipher):
    
    def __init__(self,master,language):
        Cipher.__init__(self,master,language)
    
    def build(self):
       Cipher.build()
    
    def decrypt(self):
        result=""
        tmp=""
        code=self.encrypted.get()
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
                    pass
        try:
            result+=chr(64+int(tmp))
        except:
            pass
        self.decrypted.delete(0,"end")
        self.decrypted.insert(0,result)

class Vigenere_Cipher(Cipher):

    def __init__(self, master, language):
        super().__init__(master, language)
        self.lkey=tkinter.Label(self.frame,anchor="w",bg="#262626",fg="#FFFFFF",font=("Courier",16),text="Key")#language[Controller.cur_language]["lkey"])
        self.key=tkinter.Entry(self.frame,font=("Courier",16), bg="#262626", fg="#FFFFFF")

    def build(self):
        self.frame.place(x=0,y=0,anchor="nw")
        self.lencrypted.place(x=0,y=10,anchor="nw",width=200,height=20)
        self.ldecrypted.place(x=0,y=90,anchor="nw",width=200,height=20)
        self.encrypted.place(x=201,y=10,anchor="nw",width=330,height=20)
        self.decrypted.place(x=201,y=90,anchor="nw",width=330,height=20)
        self.execute.place(x=0,y=130,anchor="nw",width=580,height=50)
        self.quit.place(x=560,y=0,anchor="nw",width=20,height=20)
        self.lkey.place(x=0,y=50,anchor="nw",width=200,height=20)
        self.key.place(x=201,y=50,anchor="nw",width=330,height=20)  
        
    def decrypt(self):
        en_text = self.encrypted.get()
        de_text = self.decrypted.get()
        key = self.key.get()
        if de_text != "" and en_text != "":
            self.encrypted.insert(0, "Error u can't enter both")
            self.decrypted.insert(0, "") 
        elif de_text == "" and en_text != "":
            self.decrypted.insert(0, self.decode(en_text, key))
        elif en_text == "" and de_text != "":
            self.encrypted.insert(0, self.encode(de_text, key))
        else:
            self.encrypted.insert(0, "unexpected Error")
            self.decrypted.insert(0, "") 

    def decode(self, code: str, key: str) -> str :
        result = ""
        lenght = len(code)
        extra_letters = ["!", ".", ",", ":", ";"]
        i = 0

        for _ in extra_letters:
            code = code.replace(_, "")
        code = code.upper()
        key = key.upper()
        while i < lenght:
            for _ in key:
                if i < lenght:
                    tmp_key = ord(_) - 65
                    tmp_result = ord(code[i]) - tmp_key
                    if (tmp_result < 65):
                        tmp_result += 26
                    result += chr(tmp_result)
                else:
                    break
                i+=1
        return result

    def encode(self, plain_text: str, key: str) -> str :
        result = ""
        lenght = len(plain_text)
        extra_letters = ["!", ".", ",", ":", ";"]
        i = 0

        for _ in extra_letters:
            plain_text = plain_text.replace(_, "")
        plain_text = plain_text.upper()
        key = key.upper()
        while i < lenght:
            for _ in key:
                if i < lenght:
                    tmp_key = ord(_) - 65
                    tmp_result = ord(plain_text[i]) + tmp_key
                    if (tmp_result > 91):
                        tmp_result -= 26
                    result += chr(tmp_result)
                else:
                    break
                i+=1
        return result