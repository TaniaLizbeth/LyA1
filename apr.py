import random
def Proyecto1():
    
    abecedario=["A","B","C","D","E","F"]
    a=0
    b=int(input("Ingresa el numero de palabras deseadas" + "--"))
    lista=[]
    Letra=""
    while a<b:
             
        for i in range(a,b):
            #lista.append(random.choice(abecedario))
            Letra=Letra+random.choice(abecedario)
            if Letra not in lista:
            
            #print(Letra)
                lista.append(Letra)
                a=a+1
                
            else:
                
                Letra=""
    print(lista)

from time import time 
start = time()

Proyecto1()

end=time()-start
print(end)