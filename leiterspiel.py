import pre_file
def gldbchscnjctr():
	eingabe = input("Welche Zahl möchtest du als Summe zweier Primzahlen ausgegeben bekommen?\n")
	eingabe = int(eingabe)
	if eingabe in primes.plist():
    		print("Die eingebenene Zahl ist bereits eine Primzahl")
	elif eingabe not in primes.plist():
    		for h in range(len(primes.plist())):
            		if eingabe < primes.plist()[h]:
                		pO = primes.plist()[h-1]
    		for pU in primes.plist():
        		for h in range(len(primes.plist())):
            			if eingabe < primes.plist()[h]:
                			pO = primes.plist()[h-1]
            			if pO+pU == eingabe:
                			print(eingabe, " = ", pU, " + ",pO)
