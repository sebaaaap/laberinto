import logica as fun

namefile =input('ingrese el nombre del archivo: ')

resultado = fun.leer(namefile)

if resultado != None : 
   movimientos = fun.recolectarmovs(resultado)
#    print(movimientos)
   laberinto = fun.crearmatriz(resultado)
#    print(laberinto)
   inicio = fun.buscarInicio(laberinto)
#    print(inicio)
   contenido = fun.verificar_ubicacion(laberinto, inicio)
#    print(contenido)
   llave = fun.recogerllave(contenido)
#    print(llave)
   avanzar = fun.run(contenido)
#    print(avanzar)

   total = fun.points_total(['a','b','c'])
#    print(total)


#    result = fun.moverse2(laberinto, inicio, movimientos)
#    print(result)

   prueba = fun.ejecutar(movimientos,inicio,laberinto,'2')
   

else:
   print('file sin contenido lol')