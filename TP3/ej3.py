datos = open("./datos.txt","r").read()

print([x for x in datos.split("\n") if len(x) > 0])