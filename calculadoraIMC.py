#Calculadora de IMC
# IMC = peso / (altura * altura )
# <19 delgadez
# entre 20 y 25 normal
# entre 26 y 30 sobrepeso
# > 30 obesidad
def calculoMasaCorporal(p, a):
    a = a / 100
    i = p / (a * a)
    return i


def pedirIMC():
    peso = float(input('Introduce tu peso en kg: '))
    altura = int(input('Introduce tu altura en cm: '))
    imc = calculoMasaCorporal(peso, altura)
    print('Valor de IMC: ' + str(imc))
    if imc <= 19:
        print('delgadez')
    else:
        if 20 <= imc <= 25:
            print('normal')
        else:
            if 26 < imc < 30:
                print('sobrepeso')
            else:
                print('obesidad')


print('Programa para calcular tu IMC')
pedirIMC()




