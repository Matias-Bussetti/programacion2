
def checkPrimo(x):
    rtn = True
    count = 0
    ite = 0
    while ite < x-1 and count < 2:
        ite += 1
        if x % ite == 0:
            count += 1
            #print(x , "%" , ite, "count + 1 = ", count)
        #else:
            #print(x , "%" , ite)

    if count == 2:
        rtn = False
    return rtn

lista = list(range(int(input("Num: "))))
print([x for x in lista if checkPrimo(x)])