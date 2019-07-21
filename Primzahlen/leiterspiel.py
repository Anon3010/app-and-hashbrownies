import pri_file
def gldbchscnjctr():
	eingabe = input("Welche Zahl möchtest du als Summe zweier Primzahlen ausgegeben bekommen?\n")
	eingabe = int(eingabe)
	func=pri_file.Primes()
	funcpliste = func.pliste()#.split(",")
	for i in range(len(funcpliste)):
		funcpliste[i] = int(funcpliste[i])
	if eingabe in funcpliste:
		print("Die eingebenene Zahl ist bereits eine Primzahl")
	elif eingabe not in funcpliste:
		for h in range(len(funcpliste)):
			if eingabe < funcpliste[h]:
				pO = funcpliste[h-1]
		for pU in funcpliste:
			for h in range(len(funcpliste)):
				if eingabe < funcpliste[h]:
					pO = funcpliste[h-1]
				if pO+pU == eingabe:
					print(eingabe, " = ", pU, " + ",pO)
					return 1
	return 0