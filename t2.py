
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
              if fila[j] == 'E' : 
                   return (i,j)
              
    return None

def verificar_ubicacion(matriz, cordenada):
     fila = cordenada[0]
     colum = cordenada[1]
     contenido = matriz[fila][colum]
     if contenido == None:
          return None
     return contenido

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
          if letra == 'b':
               total += 1000
          if letra == 'c':
               total += 100
          else:
               total +=0
     return total

def ejecutar(movimientos, inicio, laberinto, opcion):
    if opcion == '1':  # No pesca ni K ni P
        resultado_1 = moverse(laberinto, inicio, movimientos)
        if resultado_1[0]:
            print(f'Coordenadas: {resultado_1[1]},{resultado_1[2]}')
            print('Ha logrado salir!')
        else:
            print(f'Coordenadas: {resultado_1[1]},{resultado_1[2]}')

    elif opcion == '2':  # Pesca K y P
        resultado_2 = moverse2(laberinto, inicio, movimientos)
        if resultado_2[0]:
            print(f'Coordenadas: {resultado_2[1]},{resultado_2[2]}')
            print('Ha logrado salir!')
        else:
            print(f'Coordenadas: {resultado_2[1]},{resultado_2[2]}')

    elif opcion == '3':  # Igual, y recolecta puntos
        resultado_3 = moverse3(laberinto, inicio, movimientos)
        if resultado_3[0]:
            score = points_total(resultado_3[3])
            print(f'Coordenadas: {resultado_3[1]},{resultado_3[2]}')
            print('Ha logrado salir!')
            print(f'Puntaje: ',score)
        else:
            score = points_total(resultado_3[3])
            print(f'Coordenadas: {resultado_3[1]},{resultado_3[2]}')
            print(f'Puntaje: ',score)

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

def verificar_ubicacion2(matriz, cordenada):
    fila, colum = cordenada
    if 0 <= fila < len(matriz) and 0 <= colum < len(matriz[0]):
        return matriz[fila][colum]
    return None


def moverse2(laberinto, inicio, movimientos):
    fila, columna = inicio
    salio = False
    llave = 0  # Indica si ya se recogió la llave

    for letra in movimientos:
        newfila, newcolumna = fila, columna

        # Determinar nueva posición basada en el movimiento
        if letra == 'W':  # Arriba
            newfila -= 1
        elif letra == 'S':  # Abajo
            newfila += 1
        elif letra == 'A':  # Izquierda
            newcolumna -= 1
        elif letra == 'D':  # Derecha
            newcolumna += 1

        # Validar si la nueva posición está dentro de los límites
        contenido = verificar_ubicacion2(laberinto, (newfila, newcolumna))
        if contenido is not None:  # Solo se ejecuta si la posición es válida
            if contenido != '*':  # No es una pared
                if contenido == 'K':  # Recoger llave
                    llave += 1
                elif contenido == 'P':  # Puerta
                    if llave > 0:
                        llave -= 1  # Usar una llave
                    else:
                        # No se puede pasar, regresar a la posición anterior
                        newfila, newcolumna = fila, columna
                elif contenido == 'S':  # Salida
                    salio = True
                    return salio, newfila, newcolumna

                # Actualizar la posición
                fila, columna = newfila, newcolumna

    return salio, fila, columna




def moverse3(laberinto, inicio, movimientos):
    fila, columna = inicio
    salio = False
    llave = 0  # Indica si ya se recogió la llave
    puntos = []

    for letra in movimientos:
        newfila, newcolumna = fila, columna

        # Determinar nueva posición basada en el movimiento
        if letra == 'W':  # Arriba
            newfila -= 1
        elif letra == 'S':  # Abajo
            newfila += 1
        elif letra == 'A':  # Izquierda
            newcolumna -= 1
        elif letra == 'D':  # Derecha
            newcolumna += 1

        # Validar si la nueva posición está dentro de los límites
        contenido = verificar_ubicacion2(laberinto, (newfila, newcolumna))
        if contenido is not None:  # Solo se ejecuta si la posición es válida
            if contenido != '*':  # No es una pared
                if contenido == 'K':  # Recoger llave
                    llave += 1
                if contenido == 'a':
                    puntos.append(contenido)
                if contenido == 'b':
                    puntos.append(contenido)
                if contenido == 'c':
                    puntos.append(contenido)

                elif contenido == 'P':  # Puerta
                    if llave > 0:
                        llave -= 1  # Usar una llave
                    else:
                        # No se puede pasar, regresar a la posición anterior
                        newfila, newcolumna = fila, columna
                elif contenido == 'S':  # Salida
                    salio = True
                    return salio, newfila, newcolumna, puntos

                # Actualizar la posición
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