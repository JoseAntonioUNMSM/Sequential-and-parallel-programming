from MergeSort import merge_sort
from multiprocessing import Pool
import time

# Función para separar las cartas por palo
def separar_cartas(trozo_cartas):
    corazones, diamantes, treboles, espadas, jokers = [], [], [], [], []
    for carta in trozo_cartas:
        match carta[1]:
            case 'Corazones':
                corazones.append(carta)
            case 'Diamantes':
                diamantes.append(carta)
            case 'Treboles':
                treboles.append(carta)
            case 'Espadas':
                espadas.append(carta)
            case _:  
                jokers.append(carta)
    return corazones, diamantes, treboles, espadas, jokers

def ordenar_palo(cartas):
    merge_sort(cartas)
    return cartas

# Función principal para ordenar cartas en paralelo
def ordenar_barajas_paralela(cartas_totales):
    # Dividir las cartas totales en 4 trozos
    trozos = [cartas_totales[i::4] for i in range(4)]

    # Separar las cartas por palo en paralelo
    inicio_proceso = time.time()
    with Pool(4) as pool:
        resultados_separacion = pool.map(separar_cartas, trozos)
        
    # Combinar los resultados de la separación
    cartas_corazones = sum((resultado[0] for resultado in resultados_separacion), [])
    cartas_diamantes = sum((resultado[1] for resultado in resultados_separacion), [])
    cartas_treboles = sum((resultado[2] for resultado in resultados_separacion), [])
    cartas_espadas = sum((resultado[3] for resultado in resultados_separacion), [])
    cartas_joker = sum((resultado[4] for resultado in resultados_separacion), [])

    with Pool(4) as pool:
        resultados = pool.map(ordenar_palo, [cartas_corazones, cartas_diamantes, cartas_treboles, cartas_espadas])

    # Combinar los resultados en el orden deseado
    cartas_ordenadas = sum(resultados,[]) + cartas_joker
    fin_proceso = time.time()

    print("Cantidad de cartas ordenadas : " ,len(cartas_ordenadas) )
    print("Tiempo Total: {:.4f} segundos".format(fin_proceso - inicio_proceso))
    
    return cartas_ordenadas
