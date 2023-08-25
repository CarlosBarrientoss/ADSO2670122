positivo=0
negativo=0
while True:
    print ("ingrese un numero: ")
    print ("el 0 cierra el programa")
    num =int(input())
    if num==0:
        print("cerrando programa")
        break
    elif num>0:
        positivo+=num
    else :
        negativo+=1
    print ("la suma de los positivos: "+str(positivo))
    print ("la cantidad de los negativos: "+str(negativo))
        
        
    
    