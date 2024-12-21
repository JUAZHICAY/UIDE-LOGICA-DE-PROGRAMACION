import random #llamdo de funcion para numeros aleatorios
import os # llamado de funciones para manipular archivos y directorios

print("JUEGO DE PIEDRA PAPEL O TIJERA")  # Encabezado
print("ELIJA UNA OPCION")  # Encabezado
print("1 JUGAR")  # Encabezado
print("2 SALIR")  # Encabezado

op = int(input("Escoja la opcion: "))  # Se escoge la opción para jugar
print("Su respuesta es: ", op)  # Se lee la respuesta
os.system('cls')  # Limpia la pantalla

if op == 1:
    print("****************************************")# Encabezado
    print("**  UIDE ** ")# Encabezado
    print("COMO QUIERES JUGAR?")# Encabezado
    print("1 = CON LA MAQUINA")# Opcion para jugar con maquina
    print("2 = ENTRE 2 JUGADORES")# Opcion para jugar con otro jugador

    op1 = int(input("ESCOGE LA OPCION: "))  # Se escoge la opción para jugar
    os.system('cls')  # Limpia la pantalla

    if op1 == 1:
        print("**  UIDE ** ")# Encabezado
        print("** MAQUINA - USUARIO **")# Encabezado
        print("BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA")# Encabezado
        print("INSTRUCCIONES")# Encabezado
        print("SELECCIONA UNA DE LAS SIGUIENTES OPCIONES")# Encabezado
        print("1 = PIEDRA")# Encabezado
        print("2 = PAPEL")# Encabezado
        print("3 = TIJERA")# Encabezado

        while True:  # Bucle infinito hasta que decidan salir
            t1 = int(input("Turno Jugador: "))  # Elección del jugador 
            if t1 not in [1, 2, 3]:# Validar la entrada del jugador
                print("Elección inválida. Por favor, elige entre 1, 2 y 3.")#imprime mensaje
                continue          
            t2 = random.randint(1, 3)# Elección aleatoria de la computadora
            opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}#creacion de un diccinario
            print(f"La computadora eligió: {opciones[t2]}")#imprime la eleccion realizada

            # Determinar el ganador
            if t1 == 1 and t2 == 2:#COMPARACION ENTRE PIEDRA Y PAPEL
                print("El Ganador entre PIEDRA Y PAPEL es: COMPUTADORA (PAPEL)")
            elif t1 == 1 and t2 == 3:#COMPARACION ENTRE PIEDRA Y TIJERA
                print("El Ganador entre PIEDRA Y TIJERA es: JUGADOR (PIEDRA)")
            elif t1 == 2 and t2 == 1:#COMPARACION ENTRE PAPEL Y PIEDRA
                print("El Ganador entre PAPEL Y PIEDRA es: JUGADOR (PAPEL)")
            elif t1 == 2 and t2 == 3:#COMPARACION ENTRE PAPEL Y TIJERA
                print("El Ganador entre PAPEL Y TIJERA es: COMPUTADORA (TIJERA)")
            elif t1 == 3 and t2 == 1:#COMPARACION ENTRE TIJERA Y PIEDRA
                print("El Ganador entre TIJERA Y PIEDRA es: COMPUTADORA (PIEDRA)")
            elif t1 == 3 and t2 == 2:#COMPARACION ENTRE TIJERA Y PAPEL
                print("El Ganador entre TIJERA Y PAPEL es: JUGADOR (TIJERA)")
            elif t1 == t2:#COMPARACION  SI SON IGUALES
                print(f"ES UN EMPATE ({opciones[t1]})")
            # Preguntar si el jugador quiere jugar otra vez y me controla que el valor de entrada este en 
            #letras minusculas para que funcioneel bucle
            jugar_otra_vez = input("¿Quieres jugar otra vez? (s/n): ").strip().lower()
            if jugar_otra_vez != 's':#me verifica que la opcion del jugador sea s
                print("**  UIDE ** ")#Mensaje
                print("¡Gracias por jugar!")#mensaje
                break  # Salir del bucle si no quieren continuar

    elif op1 == 2:
        print("**  UIDE ** ")# Encabezado
        print("** OPCION - MULTIJUGADOR **")# Encabezado
        print("BIENVENIDO AL JUEGO PIEDRA PAPEL O TIJERA")# Encabezado
        print("INSTRUCCIONES")# Encabezado
        print("SELECCIONA UNA DE LAS SIGUIENTES OPCIONES")# Encabezado
        print("1 = PIEDRA")# Encabezado
        print("2 = PAPEL")# Encabezado
        print("3 = TIJERA")# Encabezado

        while True:  # Bucle infinito hasta que decidan salir
            t1 = int(input("Turno Jugador 1: "))  # Elección del jugador 1
            t2 = int(input("Turno Jugador 2: "))  # Elección del jugador 2

            print("Sus respuestas son:  JUGADOR 1:", t1, "  JUGADOR 2:", t2)#imprime las respuesta ingresadas

            if t1 == 1 and t2 == 2:#COMPARACION ENTRE PIEDRA Y PAPEL
                print("El Ganador entre PIEDRA Y PAPEL es: JUGADOR 2 (PAPEL)")
            elif t1 == 1 and t2 == 3:#COMPARACION ENTRE PIEDRA Y TIJERA
                print("El Ganador entre PIEDRA Y TIJERA es: JUGADOR 1 (PIEDRA)")
            elif t1 == 2 and t2 == 1:#COMPARACION ENTRE PAPEL Y PIEDRA
                print("El Ganador entre PAPEL Y PIEDRA es: JUGADOR 1 (PAPEL)")
            elif t1 == 2 and t2 == 3:#COMPARACION ENTRE PAPEL Y TIJERA
                print("El Ganador entre PAPEL Y TIJERA es: JUGADOR 2 (TIJERA)")
            elif t1 == 3 and t2 == 1:#COMPARACION ENTRE TIJERA Y PIEDRA
                print("El Ganador entre TIJERA Y PIEDRA es: JUGADOR 2 (PIEDRA)")
            elif t1 == 3 and t2 == 2:#COMPARACION ENTRE TIJERA Y PAPEL
                print("El Ganador entre TIJERA Y PAPEL es: JUGADOR 1 (TIJERA)")
            elif t1 == t2:#COMPARACION  SI SON IGUALES
                print("ES UN EMPATE")

            # Preguntar si los jugadores quieren jugar otra vez
            jugar_otra_vez = input("¿Quieren jugar otra vez? (s/n): ").strip().lower()
            if jugar_otra_vez != 's':#me verifica que la opcion del jugador sea s
                print("**  UIDE ** ")#Mensaje
                print("¡Gracias por jugar!")#Mensaje
                break  # Salir del bucle si no quieren continuar

else:
    print("**  UIDE ** ")
    print("REGRESA PRONTO")