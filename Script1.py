##Demetrio Torres Yanahi
#Cada jugador tiene nombre, set, puntos y juegos

jugador1 = input("¿Cuál es el nombre del Jugador 1? " )
j1Set = 0
j1Puntos = 0
j1Juegos = 0

jugador2 = input("¿Cuál es el nombre del Jugador 2? " )
j2Set = 0
j2Puntos = 0
j2Juegos = 0

saque = 1



#Cambiar el servicio
def cambioCancha():
    if (j1Set + j2Set) % 2 != 0:
        print("Cambio de cancha")
    else:
        print("Permanecemos en la misma cancha")
        

#Convertimos los punto 1.-15 2.30 3.40 4.Adv
def convertirPuntos(puntos):
    if puntos == 0:
        return "0"
    elif puntos == 1:
        return "15"
    elif puntos == 2:
        return "30"
    elif puntos == 3:
        return "40"
    elif puntos ==4:
        return "Adv"
    
#Cambiar el servicio
def cambioSaque():
    global saque
    if saque == 1:
        saque=2
    else:
        saque = 1

def ganarPartido(sets1, sets2):
    if sets1 == 2:
        print("jugador1 gana el encuentro.")
    elif sets2 == 2:
        print("jugador2 gana el encuentro.")




def anotarSet(j1Juego, j2Juego):
    global j1Set
    global j2Set
    global j1Juegos
    global j2Juegos
    if (j1Juego >= 6 and j1Juego >= j2Juego + 2) or (j2Juego >= 6 and j2Juego >= j1Juego + 2):
        if j1Juego > j2Juego:
            j1Set += 1
            print(f"{jugador1} ha ganado el set.")
            ganarPartido(j1Set, j2Set)
            if j1Set == 2:
                print(jugador1 + " ha ganado el partido")
        else:
            j2Set += 1
            print(f"{jugador2} ha ganado el set.")
            if j1Set == 2:
                print(jugador1 + " ha ganado el partido")

        j1Juegos = 0
        j2Juegos = 0




def anotarJuego(puntos1, puntos2):
    global j1Puntos, j2Puntos, j1Juegos, j2Juegos
    if puntos1 == 4:
        print(jugador1 +"Ganó el juego")
        j1Juegos += 1
        cambioSaque()
        anotarSet(j1Juegos, j2Juegos)


    if puntos1 >= 4 and puntos1 >= puntos2 + 2:
        print(jugador2 +"Ganó el juego")
        j2Juegos += 1
        cambioSaque()
        anotarSet(j1Juegos, j2Juegos)



    elif puntos2 >= 4 and puntos2 >= puntos1 + 2:
        j2Juegos += 1
        j1Puntos = 0
        j2Puntos = 0
    elif puntos1 == 3 and puntos2 == 3:
        print("Deuce")
    elif puntos1 >= 4 and puntos2 >= 4:
        if puntos1 == puntos2 + 1:
            print("Ventaja Jugador 1!")
        elif puntos2 == puntos1 + 1:
            print("Ventaja Jugador 2!")                





##Imprime el marcador del juego
def imprimirMarcador(jugador1,jugador2):
    if saque == 1:
        print(f"{jugador1} tiene el saque")
    else:
        print(f"{jugador2} tiene el saque")
    print(jugador1 +" tiene " )
    print("Sets ganados: " + str(j1Set))
    print("Puntos a favor: " + str(convertirPuntos(j1Puntos)))
    print("Juegos: " + str(j1Juegos))

    print("\n" + jugador2 +"  tiene" )
    print("Sets ganados: " + str(j2Set))
    print("Puntos: " + str(convertirPuntos(j2Puntos)))
    print("Juegos: " + str(j2Juegos))


def ganarPunto(ganador_punto, puntaje1, puntaje2):
    global  j1Puntos 
    global j2Puntos 
    if ganador_punto == 1:
        if (puntaje2 == 3) & (puntaje1 == 3):
            j1Puntos = 10 #10 es Advantage
        elif (puntaje1 == 3) & (puntaje2 == 10):
            j2Puntos = 3
        elif (puntaje1 == 10):
            j1Puntos = 4
            anotarJuego(j1Puntos, j2Puntos)
            j1Puntos = 0
            j2Puntos = 0
        elif (puntaje1 == 3) & (puntaje2 <= 2):
            j1Puntos+= 1
            anotarJuego(j1Puntos, j2Puntos)
            j1Puntos = 0
            j2Puntos = 0
        else:
            j1Puntos += 1

    if ganador_punto == 2:
        if (puntaje1 == 3) & (puntaje2 == 3):
            j2Puntos = 10 #10 es Advantage
        elif (puntaje2 == 3) & (puntaje1 == 10):
            j1Puntos = 3
        elif (puntaje2 == 10):
            j2Puntos = 4
            anotarJuego(j1Puntos, j2Puntos)
            j2Puntos = 0
            j1Puntos = 0
        elif (puntaje2 == 3) & (puntaje1 <= 2):
            j2Puntos+= 1
            anotarJuego(j1Puntos, j2Puntos)
            j2Puntos = 0
            j1Puntos = 0
        else:
            j2Puntos += 1
    
# Loop para registrar los puntos
while True:
    cambioCancha();
    try:
        puntoPara = int(input(f"¿Quién gana el punto, {jugador1} (1) o {jugador2}? (2)"))
        if puntoPara == 1:
            ganarPunto(puntoPara, j1Puntos, j2Puntos)
        elif puntoPara == 2:
            ganarPunto(puntoPara, j1Puntos, j2Puntos)
        else:
            raise    
    except:
        print("Nombre de jugador inválido")
    
    imprimirMarcador(jugador1, jugador2)

print("Fin del partido")

