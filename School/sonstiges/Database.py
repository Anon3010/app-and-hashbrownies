import mysql.connector, Lib.tkinter, sys
from Lib.tkinter import messagebox

class BaseConnector(Lib.tkinter.Tk):
    def __init__(self):
        super().__init__("PyMySQLHub")
        self.bt_connect=Lib.tkinter.Button(self, text="connect", command=self.connect)
        self.bt_quit=Lib.tkinter.Button(self, text="quit", command=self.destroy)
        self.lb_host=Lib.tkinter.Label(self, text="Host:")
        self.lb_passwd=Lib.tkinter.Label(self, text="Password")
        self.lb_user=Lib.tkinter.Label(self, text="User:")
        self.en_host=Lib.tkinter.Entry(self, relief="sunken", justify="left")
        self.en_passwd=Lib.tkinter.Entry(self, relief="sunken", justify="left")
        self.en_user=Lib.tkinter.Entry(self, relief="sunken", justify="left")
        
        self.bt_connect.grid(row=3, column=1)
        self.bt_quit.grid(row=3, column=2)
        self.lb_host.grid(row=0, column=0)
        self.lb_passwd.grid(row=2, column=0)
        self.lb_user.grid(row=1, column=0)
        self.en_host.grid(row=0, column=1, columnspan=2)
        self.en_passwd.grid(row=2, column=1, columnspan=2)
        self.en_user.grid(row=1, column=1, columnspan=2)
        self.geometry("193x93")
        
    

    def connect(self):
        host=self.en_host.get()
        user=self.en_user.get()
        passwd=self.en_passwd.get()
        try:
            if (host == "LOCALHOST"):
                host="127.0.0.1"
            mysql.connector.connect\
                (host=host, user=user, passwd=passwd)
        except:
            messagebox.showerror("Connection Error",\
                "Connection Error!\nCheck your inputs\nHint: You can use \"LOCALHOST\" for 127.0.0.1")
                   
    
    # def getFrameSize(self):
    #     print(self.winfo_geometry())

Lib.tkinter.Toplevel
        
    
        
BaseConnector().mainloop()