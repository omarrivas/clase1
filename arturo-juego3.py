
#CON CICLO Y PUNTAJE

import random

#Primero Arturo se presenta
print("Hola, soy Arturo. Voy a elegir un lugar para esconderme del 1 al 5:")
print("1 es el Comedor")
print("2 es la Cocina")
print("3 es el Jardin")
print("4 es el Dormitorio")
print("5 es el Baño")

puntajeArturo= 0
puntajeUsuario= 0

#Arturo elige un escondite
esconditeArturo= random.randint(1,5)

#Pregunto donde se escondio
eleccionUsuario= int(input("Por favor dime donde crees que arturo se escondió (del 1 al 5) o escribe 0 para salir:"))

while eleccionUsuario!= 0:
    #Se escondio en el baño?
    if esconditeArturo == 5:
        print("Disculpa, Arturo se escondio en el baño. Comienza de nuevo.")
        eleccionUsuario = int(input("Por favor dime donde crees que arturo se escondió (del 1 al 5) o escribe 0 para salir:"))
    else:
        if esconditeArturo == eleccionUsuario:
            puntajeUsuario= puntajeUsuario + 1
            print("LO ENCONTRASTE!!! BIEN!")
            print("Puntaje: Arturo " + str(puntajeArturo) + " versus Tu " + str(puntajeUsuario))
            eleccionUsuario = int(input("Por favor dime donde crees que arturo se escondió (del 1 al 5) o escribe 0 para salir:"))
            #Arturo elige un escondite
            # esconditeArturo= random.randint(1,5)
        else:
            puntajeArturo= puntajeArturo + 1
            print("NO LO ENCONTRASTE ARTURO ESTABA EN: " + str(esconditeArturo))
            print("Puntaje: Arturo " + str(puntajeArturo) + " versus Tu " + str(puntajeUsuario))
            eleccionUsuario = int(input("Por favor dime donde crees que arturo se escondió (del 1 al 5) o escribe 0 para salir:"))
            #Arturo elige un escondite
            esconditeArturo= random.randint(1,5)

print("Gracias por jugar!")