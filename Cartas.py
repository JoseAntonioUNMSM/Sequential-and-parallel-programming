# BARAJA DE CARTAS
import random

#Crear los 4 palos de una baraja de cartas
palos = ['Corazones', 'Diamantes', 'Treboles', 'Espadas']

# Números de las cartas
numeros = list(range(1, 14))

def generar_baraja() :
    # Generar una baraja completa de 52 cartas
    carta = [ (numero,palo) for palo in palos for numero in numeros ]
    # Añadir los 2 jokers correspondientes a una baraja de cartas , la baraja completa tiene 54 cartas
    carta.append((0, 'Joker'))
    carta.append((0, 'Joker'))
    return carta

def generar_barajas_totales(num_barajas):
    # Pasaremos por parametro el num_barajas que queremos obtener
    carta = generar_baraja()
    cartas_totales = carta * num_barajas
    random.shuffle(cartas_totales)
    return cartas_totales