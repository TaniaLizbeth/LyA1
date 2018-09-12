def Proyecto2():

   
    palabras=[input("Ingresa el Alfabeto")]
    
    cadena=[]
    
    for i in (palabras):
        b=i
        for j in b:
            if j not in (cadena):
                cadena.append(j)
    print(cadena)
    
from time import time 
start = time()

Proyecto2()

end=time()-start
print(end)