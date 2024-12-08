#JUEGO PIEDRA PAPEL O TIJERA

print("JUEGO DE PIEDRA PAPEL O TIJERA") #encabezado
print("ELIJA UNA OPCION ") #encabezado
print("1 JUGAR") #encabezado
print("2 SALIR") #encabezado
op = int(input("escoja la opcion "))  #Se escoje la opcion para jugar
print("Su respuesta es  ",+ op) #se lee la respuesta
print==(op)#declaracion de variables
if op==1:
    print("BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA")
    print("INSTRUCCIONES")#instrucciones
    print(" 1= PIEDRA")
    print(" 2= PAPEL")
    print(" 3= TIJERA")
    t1 = int(input("Turno Maquina "))#variable maquina
    t2 = int(input("Turno Usuario "))#variable usuario
    print("Sus respuestas son:  ","MAQUINA: ", + t1,"  ","USUARIO:  ",+t2)

if t1 == 1 and t2 == 2:
    print("El ganador es  :  ", t2)
elif t1 == 1 and t2 == 3:
    print("El ganador es  :", t1)
elif t1 == 2 and t2 == 1:
    print("El ganador es  :", t1 )
elif t1 == 2 and t2 == 3:
    print("El ganador es  : ", t2)
elif t1 == 3 and t2 == 1:
    print("El ganador es  :", t1)
elif t1 == 3 and t2 == 2:
    print("El ganador es  :", t1)
elif t1 == t2:


   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    """if t1==t2:#condiciones
        print("EMPATE")
    else:
        a= 1
        b= 2
        c= 3
        if t2 == a:
            if t1== 2:
                  print("GANA MAQUINA")
            else :
                  print("GANA USUARIO")      
        else :
              print("t")   

else :
    print("REGRESA PRONTO")"""