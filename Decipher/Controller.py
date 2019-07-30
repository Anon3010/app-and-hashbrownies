import tkinter
from ATBASH import Atbash_Cipher
from CAESAR import Caesar_Cipher
from A1Z26 import A1Z26_Cipher

class Controller:
    stat=""
    def __init__(self,root):
        self.root=root
        self.caesar=Caesar_Cipher(self.root)
        self.atbash=Atbash_Cipher(self.root)
        self.a1z26=A1Z26_Cipher(self.root)
        self.Menu=tkinter.Menu(self.root)
        #Menu Punkte
        self.MF1=tkinter.Menu(master=self.Menu)
        self.MF2=tkinter.Menu(master=self.Menu)
        #Funktionen des Menus
        self.MF2.add_command(label="Caesar crypt",command=lambda x="CAESAR": self.Create(x))
        self.MF2.add_command(label="Atbash crypt",command=lambda x="ATBASH": self.Create(x))
        self.MF2.add_command(label="A1Z26 crypt",command=lambda x="A1Z26": self.Create(x))
        self.MF1.add_command(label="beenden", command=self.root.destroy)
        
        self.root.geometry("800x800")
        self.Menu.add_cascade(label="Menu",menu=self.MF1)
        self.Menu.add_cascade(label="Mode",menu=self.MF2)
        self.root["menu"]=self.Menu
        self.root.mainloop()

    def Create(self,mode):
        if mode== self.stat:
            pass
        else:
            if mode=="CAESAR":
                self.caesar.build()
                self.stat="CAESAR"
                try:
                    self.atbash.frame.grid_forget()
                except:
                    pass
                try:
                    self.a1z26.frame.grid_forget()
                except:
                    pass

            if mode=="ATBASH":
                self.atbash.build()
                self.stat="ATBASH"
                try:
                    self.caesar.frame.grid_forget()
                except:
                    pass
                try:
                    self.a1z26.frame.grid_forget()
                except:
                    pass

            if mode=="A1Z26":
                self.a1z26.build()
                self.stat="A1Z26"
                try:
                    self.caesar.frame.grid_forget()
                except:
                    pass
                try:
                    self.atbash.frame.grid_forget()
                except:
                    pass

            


tk=tkinter.Tk()
Controller(tk)