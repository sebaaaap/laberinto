
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

def ejecutar(movimientos, init, laberinto, opcion):
    if opcion == '1':  # No pesca ni K ni P
        resultado_1 = moverse(laberinto, init, movimientos)
        if resultado_1:
            print('Salió correctamente')
        else:
            print('No salió')

    elif opcion == '2':  # Pesca K y P
        resultado_2 = moverse2(laberinto, init, movimientos)
        if resultado_2:
            print('Salió correctamente')
        else:
            print('No salió')

    elif opcion == '3':  # Igual, y recolecta puntos
        resultado_3 = moverse3(laberinto, init, movimientos)
        if resultado_3[0]:
            score = points_total(resultado_3[1])
            print(f'Salió con un total de puntos: ', score)
        else:
            print('No salió')

    else:
        print('Ingrese una opción correcta')


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
                    else:
                        continuar = False

    return salio

def moverse2(laberinto, inicio, movimientos):
    fila = inicio[0]
    columna = inicio[1]
    continuar = True
    salio = False
    llaves = 0  # Contador de llaves recogidas

    while continuar:
        for letra in movimientos:
            # Determinar nueva posición basada en el movimiento
            if letra == 'W' and fila > 0:  # Movimiento hacia arriba
                newfila, newcolumna = fila - 1, columna
            elif letra == 'S' and fila < len(laberinto) - 1:  # Movimiento hacia abajo
                newfila, newcolumna = fila + 1, columna
            elif letra == 'A' and columna > 0:  # Movimiento hacia la izquierda
                newfila, newcolumna = fila, columna - 1
            elif letra == 'D' and columna < len(laberinto[0]) - 1:  # Movimiento hacia la derecha
                newfila, newcolumna = fila, columna + 1
            else:
                continuar = False  # Movimiento inválido
                return salio

            # Verificar contenido de la nueva posición
            contenido = verificar_ubicacion(laberinto, (newfila, newcolumna))
            verif = run(contenido)

            if verif:  # Si el movimiento es válido
                if contenido == 'K':  # Recoger llave
                    llaves += 1  # Incrementar contador de llaves
                elif contenido == 'P':  # Encontrar puerta
                    if llaves > 0:  # Solo puede avanzar si tiene al menos una llave
                        llaves -= 1  # Usar una llave para abrir la puerta
                        continuar = True  # Continúa moviéndose
                    else:  # No puede pasar sin una llave
                        print('Falta una llave')
                        continuar = False
                        return salio  # Terminar el bucle y devolver el resultado
                elif contenido == 'S':  # Encontrar salida
                    salio = True
                    continuar = False
                    return salio  # Salir del bucle y devolver el resultado

                # Actualizar posición actual
                fila, columna = newfila, newcolumna
            else:
                continuar = False  # Movimiento inválido
                return salio  # Salir del bucle y devolver el resultado

    return salio


def moverse3(laberinto, inicio, movimientos):
    fila = inicio[0]
    columna = inicio[1]
    continuar = True
    salio = False
    llave = False 
    puntos = []

    while continuar:
        for letra in movimientos:
            # Determinar nueva posición basada en el movimiento
            if letra == 'W' and fila > 0:  # Movimiento hacia arriba
                newfila, newcolumna = fila - 1, columna
            elif letra == 'S' and fila < len(laberinto) - 1:  # Movimiento hacia abajo
                newfila, newcolumna = fila + 1, columna
            elif letra == 'A' and columna > 0:  # Movimiento hacia la izquierda
                newfila, newcolumna = fila, columna - 1
            elif letra == 'D' and columna < len(laberinto[0]) - 1:  # Movimiento hacia la derecha
                newfila, newcolumna = fila, columna + 1
            else:
                continuar = False  # Movimiento inválido
                continuar = False
                return salio

            # Verificar contenido de la nueva posición
            contenido = verificar_ubicacion(laberinto, (newfila, newcolumna))
            verif = run(contenido)

            if verif:  # Si el movimiento es válido
                if contenido == 'K':  # Recoger llave
                    llave = True
                if contenido == 'P':  # Encontrar puerta
                    if llave:  # Solo puede avanzar si tiene la llave
                        llave = False
                        continuar = True # Continúa moviéndose
                    else:  # No puede pasar sin la llave
                        print('falta una llave')
                        continuar = False
                        return salio , puntos  # Terminar el bucle y devolver el resultado
                if contenido == 'a':
                    puntos.append(contenido)
                if contenido == 'b':
                    puntos.append(contenido)
                if contenido == 'c':
                    puntos.append(contenido)
                elif contenido == 'S':  # Encontrar salida
                    salio = True
                    continuar = False
                    return salio, puntos # Salir del bucle y devolver el resultado

                # Actualizar posición actual
                fila, columna = newfila, newcolumna
            else:
                continuar = False  # Movimiento inválido
                return salio  # Salir del bucle y devolver el resultado

    return salio, puntos