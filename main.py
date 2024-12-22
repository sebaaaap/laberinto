import logica as fun

namefile =input('ingrese el nombre del archivo: ')

resultado = fun.leer(namefile)

if resultado != None : 
   movimientos = fun.recolectarmovs(resultado)
#    print(movimientos[2])
   laberinto = fun.crearmatriz(resultado)
#    print(laberinto)

#    print(resultado)


else:
   print('file sin contenido lol')