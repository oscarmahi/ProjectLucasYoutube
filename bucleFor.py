array = ['banana','melon','sandia','pera']

for fruta in array:
    if fruta.endswith('a'):
        print('La fruta es: ' + fruta)
print('-------------------------')
for fruta in array:
    if fruta == 'sandia':
        break
    print('La fruta es: ' + fruta)
print('-------------------------')
array.reverse()
for fruta in array:
    print('La fruta es: ' + fruta)
print('-------------------------')
array.remove('melon')
array.append('naranja')
for fruta in array:
    print('La fruta es: ' + fruta)
print('-------------------------')
print('El primer elemento del array es: ' + array[0])
print('-------------------------')
texto = 'Hola mundo'
for letra in texto:
    print('Letra: ' + letra)
print('-------------------------')
for n in range(10):
    if n > 5:
        print(n)
print('-------------------------')
for n in range(5, 10):
    print(n)
