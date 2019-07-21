import os
import primes
class Primes(object):
    def __init__(self):
        self.PATH=r"C:\Users\CoolHack\Desktop\text.txt"
  
    def create(self):
            with open(self.PATH,"w+") as f:
                f.write(primes.pgen())
                f.close()
            
    def pliste(self): #Primzahlen Liste von bis
        try:
            f=open(self.PATH,"r+")
            data=f.read()
            pl=data.split(",")
            f.close()
        except:
            self.create()
        return pl
