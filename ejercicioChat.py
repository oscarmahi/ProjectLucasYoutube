pregunta = 'Hola'
while pregunta != '':
    pregunta = input('Introduce el texto de la pregunta y :) รณ (: -> ')
    pregunta2 = pregunta
    if ':)' in pregunta:
        pregunta2 = pregunta.replace(':)', '๐')
    if '(:' in pregunta:
        pregunta2 = pregunta.replace('(:', '๐ฐ')
    print(pregunta2)







