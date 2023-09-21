import random

def checkPrimo(x):
    rtn = True
    count = 0
    ite = 0
    while ite < x-1 and count < 2:
        ite += 1
        if x % ite == 0:
            count += 1
    if count == 2:
        rtn = False
    return rtn

aleatorio = random.randint(20, 50)

def rtnNum(minimo, maximo):
    return random.randint(minimo, maximo)

def rtnList(list):
    for i in range(1, aleatorio):
        list.append(rtnNum(200, 5000))

list1 = []
rtnList(list1)

list2 = []
rtnList(list2)

def esImpar(x):
    return x % 2 == 1

def ej4List1(lista, menor):
    rtnList = lista.copy()
    
    return list(map(lambda x: x * menor, list(filter(esImpar, rtnList))))
    

def ej4List2RtnMenorifPrimo(list):
    rtn = -1
    for i in sorted(list):
        if checkPrimo(i):
            rtn = i
    return rtn

print(ej4List1(list1, ej4List2RtnMenorifPrimo(list2)))
