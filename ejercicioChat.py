pregunta = 'Hola'
while pregunta != '':
    pregunta = input('Introduce el texto de la pregunta y :) ó (: -> ')
    pregunta2 = pregunta
    if ':)' in pregunta:
        pregunta2 = pregunta.replace(':)', '😂')
    if '(:' in pregunta:
        pregunta2 = pregunta.replace('(:', '😰')
    print(pregunta2)







