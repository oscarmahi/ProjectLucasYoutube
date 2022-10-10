#Escritura fichero de texto
file = open('texto.txt', 'w')                   #si se pone a en vez de w, es para añadir en el fichero
file.write('prueba de guardado en el archivo')
file.close()

#Lectura fichero de texto
file = open('texto.txt', 'r')
print(file.read())
file.close()


#Programa para encriptar y desencriptar un fichero de texto
def encriptar():
    print('Funcion para encriptar')

def desEncriptar():
    print('Funcion para desencriptar')





