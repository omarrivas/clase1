#BASICO

import random

#Primero Arturo se presenta
print("Hola, soy Arturo. Voy a elegir un lugar para esconderme del 1 al 5:")
print("1 es el Comedor")
print("2 es la Cocina")
print("3 es el Jardin")
print("4 es el Dormitorio")
print("5 es el Baño")

#Arturo elige un escondite
esconditeArturo= random.randint(1,5)

#Pregunto donde se escondio
eleccionUsuario= int(input("Por favor dime donde crees que arturo se escondió (del 1 al 5):"))

#Se escondio en el ba�o?
if esconditeArturo == 5:
    print("Disculpa, Arturo se escondio en el baño. Comienza de nuevo.")
else:
    if esconditeArturo == eleccionUsuario:
        print("LO ENCONTRASTE!!! BIEN!")
    else:
        print("NO LO ENCONTRASTE ARTURO ESTABA EN: " + str(esconditeArturo))
