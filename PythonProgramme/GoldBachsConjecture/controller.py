import leiterspiel
while True:
    dec=input("Wollen sie eine Zahl in Primzahlen zerlegen[y/Y]oder[n/N]:")
    if dec=="y" or dec=="Y":
       leiterspiel.gldbchscnjctr()
    elif dec=="n" or dec=="N":
        print("Fik diene mUZtr du huzrenson")
        break
    else:
        print("deine Eingabe war nicht zulässig.Try again.")
        continue
