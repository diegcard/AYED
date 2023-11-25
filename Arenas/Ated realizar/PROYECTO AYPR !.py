FILAS = 10
COLUMNAS = 10
MAR = " "
PORTAVIONES = "P"  # Ocupa cinco celdas
BUQUE_GUERRA = "B"  # Ocupa cuatro celdas
SUBMARINO_2 = "S"  # Ocupa tres celdas
DESTRUCTOR_2 = "D"  # Ocupa tres celdas
CORVETA = "C"  # Ocupa dos celdas
DISPARO_FALLADO = "-"
DISPARO_ACERTADO = "*"
DISPAROS_INICIALES = 50
CANTIDAD_BARCOS_INICIALES = 23
JUGADOR_1 = " "
JUGADOR_2 = " "


def pedir_nombres():
    JUGADOR_1 = input("Ingrese el nombre del primer jugador: ")
    JUGADOR_2 = input("Ingrese el nombre del segundo jugador: ")
    return JUGADOR_1, JUGADOR_2


def configcampo():
    
    campo = [[MAR] * COLUMNAS for _ in range(FILAS)]
    
    for i in range(FILAS):
        campo[i][-1] = str(i + 1)
    for j in range(COLUMNAS):
        campo[-1][j] = str(j + 1)
    
    return campo

    
def imprimir_tablero(campo):
    print("+---+---+---+---+---+---+---+---+---+---+")
    for i in range(len(campo)):
        if i == 0:
            print("|", " | ".join(list(map(str, campo[i]))), end=" |")
        else:
            print("|", " | ".join(list(map(str, campo[i]))), end=" |")
        print("\n+---+---+---+---+---+---+---+---+---+---+")

def colocar_barcos(JUGADOR_1, JUGADOR_2, campo):
    campo1 = [[MAR] * 10 for _ in range(10)]
    campo2 = [[MAR] * 10 for _ in range(10)]
    print("Es el turno de", JUGADOR_1, "para colocar sus barcos.")
    print("Los barcos disponibles son:")
    print("1. Portaviones (P) - ocupa cinco celdas")
    print("2. Buque de Guerra (B) - ocupa cuatro celdas")
    print("3. Submarino de 2 (S) - ocupa tres celdas")
    print("4. Destructor de 2 (D) - ocupa tres celdas")
    print("5. Corveta (C) - ocupa dos celdas")

    barcos = [(PORTAVIONES, 2)]#, (BUQUE_GUERRA, 4), (SUBMARINO_2, 3), (DESTRUCTOR_2, 3), (DESTRUCTOR_2, 3), (CORVETA, 2), (CORVETA, 2)
    for barco, tamano in barcos:
        print(f"Colocando {barco}...")
        for i in range(1, tamano + 1):
            print(f"Posicion {i} de {tamano}:")
            imprimir_tablero(campo1)
            fila = int(input("Ingrese la fila (1-10): ")) - 1
            columna = int(input("Ingrese la columna (1-10): ")) - 1
            
            while (fila < 0 or fila >= FILAS) or (columna < 0 or columna >= COLUMNAS) or campo1[fila][columna] != MAR:
                print("Posicion invalida o ya ocupada. Intente de nuevo.")
                imprimir_tablero(campo1)
                fila = int(input("Ingrese la fila (1-10): ")) - 1
                columna = int(input("Ingrese la columna (1-10): ")) - 1
                
            campo1[fila][columna] = barco

    print("Es el turno de", JUGADOR_2, "para colocar sus barcos.")
    for barco, tamano in barcos:
        print(f"Colocando {barco}...")
        for i in range(1, tamano + 1):
            print(f"Posicion {i} de {tamano}:")
            imprimir_tablero(campo2)
            fila = int(input("Ingrese la fila (1-10): ")) - 1
            columna = int(input("Ingrese la columna (1-10): ")) - 1
            
            while (fila < 0 or fila >= FILAS) or (columna < 0 or columna >= COLUMNAS) or campo2[fila][columna] != MAR:
                print("Posicion invalida o ya ocupada. Intente de nuevo.")
                imprimir_tablero(campo2)
                fila = int(input("Ingrese la fila (1-10): ")) - 1
                columna = int(input("Ingrese la columna (1-10): ")) - 1
                
            campo2[fila][columna] = barco

    return campo1, campo2

def disparar(campo, campo1, campo2, DISPAROS_INICIALES, JUGADOR_1, JUGADOR_2):
    DISPAROS_DISPONIBLES = DISPAROS_INICIALES
    puntos_J1 = 0
    puntos_J2 = 0
    campo3 = [[MAR] * 10 for _ in range(10)]
    campo4 = [[MAR] * 10 for _ in range(10)]
    turno = 0

    while DISPAROS_DISPONIBLES > 0:
        n = 0
        while n ==0:
            if turno == 0:

                print("Turno de",JUGADOR_1)
                imprimir_tablero(campo3)
                fila = int(input("Ingrese la posicion de la fila (1-10) donde quiera disparar: ")) - 1
                columna = int(input("Ingrese la posicion de la columna (1-10) donde quiera disparar: ")) - 1
            

                if (fila < 0 or fila >= FILAS) or (columna < 0 or columna >= COLUMNAS):
                    print("Posicion invalida. Intente de nuevo.")
                
                if campo3[fila][columna] == "*":
                    print('Le has dado a un lugar donde ya le diste, vuelve a intentarlo')


                if campo2[fila][columna] != MAR:
                    campo3[fila][columna] = DISPARO_ACERTADO
                    print("Le has dado a una parte de un barco.")
                    #print(campo3)
                    puntos_J1 += 1
                    turno = 0
                

                else:
                    campo3[fila][columna] = DISPARO_FALLADO
                    print("Esta vez no le diste.")
                    turno += 1
                    n = 1
            

        NN = 0
        while NN ==0:
            if turno == 1:

                print("Turno de",JUGADOR_2)
                imprimir_tablero(campo4)
                fila = int(input("Ingrese la posicion de la fila (1-10) donde quiera disparar: ")) - 1
                columna = int(input("Ingrese la posicion de la columna (1-10) donde quiera disparar: ")) - 1
            

                if (fila < 0 or fila >= FILAS) or (columna < 0 or columna >= COLUMNAS):
                    print("Posicion invalida. Intente de nuevo.")
                    continue

                if campo1[fila][columna] != MAR:
                    campo4[fila][columna] = DISPARO_ACERTADO
                    print("Le has dado a una parte de un barco.")
                    puntos_J2 += 1
                    turno = 1
                else:
                    campo4[fila][columna] = DISPARO_FALLADO
                    print("Esta vez no le diste.")
                    turno -= 1
                    NN = 1
            

        DISPAROS_DISPONIBLES -= 1
    
        if puntos_J1 == 23 or puntos_J2 == 23:

            break
    

    return puntos_J1, puntos_J2

def jugar():
    JUGADOR_1, JUGADOR_2 = pedir_nombres()
    print("Campo de batalla:\n")
    campo = configcampo()
    imprimir_tablero(campo)
    print("Inicio del juego. Primero coloque sus barcos.")
    campo1, campo2 = colocar_barcos(JUGADOR_1, JUGADOR_2, campo)
    puntos_J1, puntos_J2 = disparar(campo, campo1, campo2, DISPAROS_INICIALES, JUGADOR_1, JUGADOR_2)
    print("Fin del juego.")
    print(f"{JUGADOR_1} ha obtenido {puntos_J1} puntos.")
    print(f"{JUGADOR_2} ha obtenido {puntos_J2} puntos.")

def acerca_de():
    print("Programado por Julian Morales y Jhordan Ariza")

def main():
    print("Recuerde que antes de jugar necesito que coloquen sus nombres.")
    while True:
        print("\n\n BATALLA NAVAL.\
               \n.")
        print("\n1. Jugar.\
               \n2. Acerca de.\
               \n9. Finalizar el programa. \n")

        operacion = int(input("Seleccione una opción: "))

        if operacion == 1:
            jugar()
        elif operacion == 2:
            acerca_de()
        elif operacion == 9:
            print("Fin del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

main()