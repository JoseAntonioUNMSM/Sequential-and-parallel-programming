from MergeSort import merge_sort
from Cartas import generar_barajas_totales
from Secuencial import ordenar_barajas_secuencial
from Paralela import ordenar_barajas_paralela

if __name__ == '__main__':
    # Generar las 75000 barajas con una cantidad total de 4050000
    cartas_totales = generar_barajas_totales(75000)
    print("\nPrimeras 20 cartas generadas: " ,  cartas_totales[:20])  

    # Ordenamiento secuencial
    print("\nOrdenamiento secuencial")
    cartas_ordenadas_secuencial = ordenar_barajas_secuencial(cartas_totales)

    # Ordenamiento paralelo
    print("\nOrdenamiento paralelo")
    cartas_ordenadas_paralelamente = ordenar_barajas_paralela(cartas_totales)