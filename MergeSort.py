# Definición del Merge Sort
def merge_sort(cartas):
    if len(cartas) > 1:
        mid = len(cartas) // 2
        left_half = cartas[:mid]
        right_half = cartas[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:
                cartas[k] = left_half[i]
                i += 1
            else:
                cartas[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            cartas[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            cartas[k] = right_half[j]
            j += 1
            k += 1
