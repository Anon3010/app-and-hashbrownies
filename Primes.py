while True:
    g = input("Gib die Obergrenze für die Primzahlenliste ein \n")
    g=int(g)
    zahlen = [z for z in range(1,g)]
    primes = set()
    for zahl in zahlen:
        print(zahl)
        if zahl == 0 or zahl == 1:
            continue
        for checkIf in range(2,g):
            print(checkIf)
            if zahl%checkIf != 0:
                primes.add(zahl)
            if zahl%checkIf == 0 and zahl!= checkIf and zahl in primes:
                primes.remove(zahl)
                break
            if zahl%checkIf == 0:
                break
    print("\n","{2,",primes)
print("das sind insgesamt: ",len(primes)+1," Primzahlen")
