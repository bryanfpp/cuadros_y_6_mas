def ordenar_abs(clase_original):
    for i in range(len(clase_original)):
        min_idx = i
        for j in range(i+1, len(clase_original)):
            if abs(clase_original[j]) < abs(clase_original[min_idx]):
                min_idx = j
        clase_original[i], clase_original[min_idx] = clase_original[min_idx], clase_original[i]
    return clase_original