def fac_to(frecuencia,clases,clase):

    fre_or = []
    for elemento in clases:
        idx = clases.index(elemento)
        fas = frecuencia[idx]
        fre_or.append(fas)

    return fre_or