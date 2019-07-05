import pri_file
def gldbchscnjctr():
	eingabe = input("Welche Zahl möchtest du als Summe zweier Primzahlen ausgegeben bekommen?\n")
	eingabe = int(eingabe)
	if eingabe in Primes.plist():
    		print("Die eingebenene Zahl ist bereits eine Primzahl")
	elif eingabe not in Primes.plist():
    		for h in range(len(Primes.plist())):
            		if eingabe < Primes.plist()[h]:
                		pO = Primes.plist()[h-1]
    		for pU in Primes.plist():
        		for h in range(len(Primes.plist())):
            			if eingabe < Primes.plist()[h]:
                			pO = Primes.plist()[h-1]
            			if pO+pU == eingabe:
                			print(eingabe, " = ", pU, " + ",pO)
