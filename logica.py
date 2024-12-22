
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

def ejecutar(movimientos, laberinto, opcion):
     if opcion == '1': # no pesca ni K ni P
          print('soy la opcion: ', opcion)
     if opcion == '2': # pesca k y P
          print('soy la opcion: ', opcion)
     if opcion == '3': # = , y recolecta puntos
          print('soy la opcion: ', opcion)
     else: 
          print('ingrese una opcion correcta')

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


          