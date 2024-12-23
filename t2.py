
def leer(nombre):

        with open(nombre) as docu:

            contenido = docu.readlines()
            if len(contenido)==0 :
                return
            else:
                return contenido

def recolectarmovs(lista):
    movimientos = []
    swap = []
    swap.append(lista[0])
    letra = 0
    while letra < len(swap) and letra != '\n' : 
         movimientos = swap[letra].strip()
         letra += 1

    return movimientos

def crearmatriz(lista):
    matriz = []
    swap = []
    elemento = 1
    while elemento < len(lista):
          swap.append(lista[elemento])
          elemento += 1
    
    for fila in swap:
      matriz.append(fila.strip())  

    return matriz


def buscarInicio(matriz):
    for i in range(len(matriz)):
        fila = matriz[i]
        for j in range(len(fila)):
            if fila[j] == 'E':
                return i, j  # Devuelve los valores separados
    return -1, -1

def verificar_ubicacion(matriz, cordenada):
     fila = cordenada[0]
     colum = cordenada[1]
     contenido = matriz[fila][colum]
     if contenido == None:
          return None
     return contenido

def verificar_ubicacion2(matriz, cordenada):
    fila, colum = cordenada
    if 0 <= fila < len(matriz) and 0 <= colum < len(matriz[0]):
        return matriz[fila][colum]
    return None

def run(contenido):
     if contenido == '*':
          return None
     return True

def recogerllave(contenido):
     if contenido == 'K':
          return True
     return None


def points_total(lista):
     total = 0
     for letra in lista:
          if letra == 'a':
               total += 10000
          elif letra == 'b':
               total += 1000
          elif letra == 'c':
               total += 100
     return total

def ejecutar(movimientos, inicio, laberinto, opcion):
    if opcion == '1':  
        resultado_1 = moverse(laberinto, inicio, movimientos)
        if resultado_1[0]:
            print("Coordenadas: " + str(resultado_1[1]) + "," + str(resultado_1[2]))
            print('Ha logrado salir!')
        else:
            print("Coordenadas: " + str(resultado_1[1]) + "," + str(resultado_1[2]))

    elif opcion == '2':  
        resultado_2 = moverse2(laberinto, inicio, movimientos)
        if resultado_2[0]:
            print("Coordenadas: " + str(resultado_2[1]) + "," + str(resultado_2[2]))
            print('Ha logrado salir!')
        else:
            print("Coordenadas: " + str(resultado_2[1]) + "," + str(resultado_2[2]))

    elif opcion == '3':  
        resultado_3 = moverse3(laberinto, inicio, movimientos)
        if resultado_3[0]:
            score = points_total(resultado_3[3])
            print("Coordenadas: " + str(resultado_3[1]) + "," + str(resultado_3[2]))
            print('Ha logrado salir!')
            print("Puntaje: " + str(score))
        else:
            score = points_total(resultado_3[3])
            print("Coordenadas: " + str(resultado_3[1]) + "," + str(resultado_3[2]))
            print("Puntaje: " + str(score))
           

    else:
        return


def moverse(laberinto, inicio, movimientos):
    fila = inicio[0]
    columna = inicio[1]
    continuar = True
    salio = False
    

    while continuar:
        for letra in movimientos:
            if letra == 'W':  
                if fila > 0:  
                    newfila = fila - 1
                    contenido = verificar_ubicacion(laberinto, (newfila, columna))  
                    verif = run(contenido)
                    if verif:
                        fila -= 1  
                        win = verificar_ubicacion(laberinto, (fila, columna))
                        if win == 'S':  # Si encuentra la salida
                            salio = True
                            continuar = False
                            return salio, fila, columna
                    else:
                        continuar = False

            if letra == 'S':  
                if fila < len(laberinto) - 1:
                    newfila = fila + 1
                    contenido = verificar_ubicacion(laberinto, (newfila, columna))  
                    verif = run(contenido)
                    if verif:
                        fila += 1  
                        win = verificar_ubicacion(laberinto, (fila, columna))
                        if win == 'S':  
                            salio = True
                            continuar = False
                            return salio, fila, columna
                    else:
                        continuar = False

            if letra == 'A':  
                if columna > 0:  
                    newcolumna = columna - 1  
                    contenido = verificar_ubicacion(laberinto, (fila, newcolumna))  
                    verif = run(contenido)
                    if verif:
                        columna -= 1  
                        win = verificar_ubicacion(laberinto, (fila, columna))
                        if win == 'S':  
                            salio = True
                            continuar = False
                            return salio, fila, columna
                    else:
                        continuar = False

            if letra == 'D':  
                if columna < len(laberinto[0]) - 1:  
                    newcolumna = columna + 1  
                    contenido = verificar_ubicacion(laberinto, (fila, newcolumna))  
                    verif = run(contenido)
                    if verif:
                        columna += 1  
                        win = verificar_ubicacion(laberinto, (fila, columna))
                        if win == 'S':  
                            salio = True
                            continuar = False
                            return salio, fila, columna
                    else:
                        continuar = False

    return salio, fila, columna



def moverse2(laberinto, inicio, movimientos):
    fila, columna = inicio
    salio = False
    llave = 0  # indica si ya se recogió la llave

    for letra in movimientos:
        newfila, newcolumna = fila, columna

        # dterminar nueva posición basada en el movimiento
        if letra == 'W':  
            newfila -= 1
        elif letra == 'S':  
            newfila += 1
        elif letra == 'A':  
            newcolumna -= 1
        elif letra == 'D':
            newcolumna += 1

        
        contenido = verificar_ubicacion2(laberinto, (newfila, newcolumna))
        if contenido is not None:  
            if contenido != '*':  # no es una pared
                if contenido == 'K':  # recoger llave
                    llave += 1
                elif contenido == 'P':  # puerta
                    if llave > 0:
                        llave -= 1  # usa una llave
                    else:
                        # no se puede pasar
                        newfila, newcolumna = fila, columna

                elif contenido == 'S':  # Salio
                    salio = True
                    return salio, newfila, newcolumna

                # actualizar la posición
                fila, columna = newfila, newcolumna

    return salio, fila, columna




def moverse3(laberinto, inicio, movimientos):
    fila, columna = inicio
    salio = False
    llave = 0 
    puntos = []
    visitados = []  # lista para almacenar posiciones ya visitadas

    for letra in movimientos:
        newfila, newcolumna = fila, columna

        # determinar nueva posición basada en el movimiento
        if letra == 'W':  
            newfila -= 1
        elif letra == 'S': 
            newfila += 1
        elif letra == 'A':  
            newcolumna -= 1
        elif letra == 'D':  
            newcolumna += 1

        # validaa si la nueva posición está dentro de los límites
        contenido = verificar_ubicacion2(laberinto, (newfila, newcolumna))
        if contenido is not None and contenido != '*': 
            if contenido == 'K':  # Recoger llave
                llave += 1
            elif contenido in ['a', 'b', 'c']:  # recolectar puntos
                if (newfila, newcolumna) not in visitados:  # solo si no ha sido visitada antes
                    puntos.append(contenido)
                    visitados.append((newfila, newcolumna))  # almacenar los visitado
            elif contenido == 'P':  # encontrar puerta
                if llave > 0:  # solo puede pasar si tiene llave
                    llave -= 1
                else:
                    # no puede pasar, no actualizamos posición
                    newfila, newcolumna = fila, columna
            elif contenido == 'S':  # Encontrar salida
                salio = True
                return salio, newfila, newcolumna, puntos

            # actualizar posición solo si el movimiento es válido
            fila, columna = newfila, newcolumna

    return salio, fila, columna, puntos





print("Menu")

print("1 Solo recorrer.")

print("2 Recorrer considerando puertas.")

print("3 Considerar puertas y puntos.")

opcion =input('Ingrese el numero de su opcion: ')
namefile = input('Ingrese el nombre del archivo: ')
resultado = leer(namefile)


if resultado != None : 
   movimientos = recolectarmovs(resultado)
   laberinto = crearmatriz(resultado)
   inicio = buscarInicio(laberinto)


   prueba = ejecutar(movimientos,inicio,laberinto,opcion)