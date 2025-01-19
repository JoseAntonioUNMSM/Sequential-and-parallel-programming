from MergeSort import merge_sort
import time

# Separar las cartas por palo
def separacion_barajas(cartas_totales):
    corazones, diamantes, treboles, espadas, joker = [], [], [], [], []
    for carta in cartas_totales:
        match carta[1]:
            case 'Corazones':
                corazones.append(carta)
            case 'Treboles':
                treboles.append(carta)
            case 'Espadas':
                espadas.append(carta)
            case 'Diamantes':
                diamantes.append(carta)
            case _:
                joker.append(carta)
    return corazones, diamantes, treboles, espadas, joker

# Ordenar las cartas
def ordenar_barajas_secuencial(cartas_totales):
    inicio_proceso = time.time()

    # Separar las cartas por palo
    corazones, diamantes, treboles, espadas, joker = separacion_barajas(cartas_totales)

    # Ordenar cada lista con Merge Sort
    cartas_por_palo = [corazones, diamantes, treboles, espadas]
    for palo in cartas_por_palo:
        merge_sort(palo)

    # Combinar las listas en el orden deseado
    cartas_ordenadas = sum(cartas_por_palo, []) + joker

    fin_proceso = time.time()
    
    print("Cantidad de cartas ordenadas : " ,len(cartas_ordenadas) )
    print("Tiempo Total: {:.4f} segundos".format(fin_proceso - inicio_proceso))

    return cartas_ordenadas


