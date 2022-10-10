contador = 0
while contador < 5:
    #if contador == 3:
    #    continue
    #con este continue se vuelve a evaluar la condición y se salta el resto de sentencias de debajo del continue
    #en este caso se entraria en un bucle infinito ya que no incrementamos el contador
    if contador != 3:
        print('El valor de contador es: ' + str(contador))
    contador += 1





