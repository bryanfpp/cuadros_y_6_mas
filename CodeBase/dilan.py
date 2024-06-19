def ordenar_abs(clases):
    for i in range(len(clases)):
        min_idx = i
        for j in range(i+1, len(clases)):
            if clases[j] < clases[min_idx]:
                min_idx = j
        clases[i], clases[min_idx] = clases[min_idx], clases[i]
        
    return clases 