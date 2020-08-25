import tkinter
from Decoder import Caesar_Cipher
from Decoder import A1Z26_Cipher
from Decoder import Atbash_Cipher
from Decoder import Vigenere_Cipher

class Controller:
    active=[]
    language={"en":{"lencrypt":"Encrypted text:","ldecrypt":"Plain text:","lkey":"Key:"},
              "de":{"lencrypt":"Verschlüsselter Text:","ldecrypt":"Klarer Text:","lkey":"Schlüssel"}
              }
    cur_language="en"
    mode="alphabet"
    def __init__(self,master):
        self.root=master
        self.panel=tkinter.Frame(self.root,width=200,height=800,bd=5,bg="#262626")
        self.properties=tkinter.Text(self.panel,bd=2,bg="#262626",fg="#FFFFFF",font=("Courier",10),insertbackground="#262626",state="disabled")
        self.caesar=Caesar_Cipher(self.root,self.language)
        self.atbash=Atbash_Cipher(self.root,self.language)
        self.a1z26=A1Z26_Cipher(self.root,self.language)
        self.vigenere=Vigenere_Cipher(self.root, self.language)
        self.Menu=tkinter.Menu(self.root)
        #Menu Punkte
        self.MF1=tkinter.Menu(master=self.Menu)
        self.MF2=tkinter.Menu(master=self.Menu)
        #Funktionen des Menus
        self.MF2.add_command(label="Caesar crypt",command=lambda x="CAESAR": self.Create(x))
        self.MF2.add_command(label="Atbash crypt",command=lambda x="ATBASH": self.Create(x))
        self.MF2.add_command(label="A1Z26 crypt",command=lambda x="A1Z26": self.Create(x))
        self.MF2.add_command(label="Vigenère crypt", command=lambda x="VIGENERE": self.Create(x))
        self.MF1.add_command(label="beenden", command=self.root.destroy)
        
        self.root.geometry("800x800")
        self.Menu.add_cascade(label="Menu",menu=self.MF1)
        self.Menu.add_cascade(label="Tools",menu=self.MF2)
        self.root["menu"]=self.Menu
        self.panel.place(x=600,y=0,anchor="nw")
        self.root["bg"]="#262626"
        self.root.mainloop()

    def Create(self,mode):
        if len(self.active)>3:
            self.active[0].frame.place_forget()
        if mode=="CAESAR":
            self.active.append(self.caesar)
            self.active[len(self.active)-1].build()
        elif mode=="ATBASH":
            self.active.append(self.atbash)
            self.active[len(self.active)-1].build()
        elif mode=="A1Z26":
            self.active.append(self.a1z26)
            self.active[len(self.active)-1].build()   
        elif mode=="VIGENERE":
            self.active.append(self.vigenere)
            self.active[len(self.active)-1].build()      
tk=tkinter.Tk()
Controller(tk)
