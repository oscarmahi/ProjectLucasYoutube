nombre = input('Como te llamas?')
print('Hola' + nombre)

edad = int(input('Cuantos años tienes?'))
masDe12 = edad >= 12
respuestaHijoDelDueño = input('Eres hijo del dueño?')
esHijoDelDueño = respuestaHijoDelDueño == 'si'
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print('Ustesd puede pasar a la montaña rusa')
else:
    print('No puede pasar')


