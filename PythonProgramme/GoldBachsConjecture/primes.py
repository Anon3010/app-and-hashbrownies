def pgen():
    import sys
    # import time
    # start=time.time()
    nprimes=[]
    pri=[]
    primes=set()
    tmp,nprimes=set(),set()
    for i in range(2,1000):
        for j in range(2,1000):
            if i%j==0 and j!=i and j!=1:
                nprimes.add(str(i))
                break
            elif i%j!=0 or i==j and str(j) not in ",".join(nprimes):
                tmp.add(str(i))
    for i in tmp:
        for j in nprimes:
            if int(i)!=int(j):
                primes.add(int(i))
            elif int(i)==int(j):
                primes.remove(int(i))
                break
    for i in primes:
        pri.append(i)
    pri.sort()
    pri=str(pri)
    pri=pri.replace("[","")
    pri=pri.replace("]","")
    pri=pri.replace(" ","")
    print(pri)
    return pri
#    pri.sort()
 #   print(pri)
  #  end=time.time()-start
   # print(f"programm finished in {end}s")



