diccionario = {
    "Programar": "Programar es lo que sea",
    "POO": "Programacion orientada a objetos",
    "MVC": "Modelo vista controlador"
}

print(diccionario["POO"])

numeros = {
    '0': 'cero',
    '1': 'uno',
    '2': 'dos',
    '3': 'tres',
    '4': 'cuatro',
    '5': 'cinco',
    '6': 'seis',
    '7': 'siete',
    '8': 'ocho',
    '9': 'nueve'
}
textoFinal = ''
texto = input('Introduce el numero: ')
for letra in texto:
    textoFinal += numeros[letra] + ' '
print(textoFinal)

