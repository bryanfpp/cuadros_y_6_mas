def fac_to(frecuencia, clases, clase_original):
    fre_or = []
    for elemento in clase_original:
        idx = clases.index(elemento)
        fas = frecuencia[idx]
        fre_or.append(fas)
        
    return fre_or