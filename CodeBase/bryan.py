def frec_abs(ls):
    
    '''
    Hola si tienes algun error concata con el podosicimo POE.com
    o comunicate con tu profe cuadros :)
    '''

    clase,frecuencia= [],[]
    for elemento in ls:    
        if elemento not in clase:
            clase.append(elemento)
            frecuencia.append(1)
        else:
            inde = clase.index(elemento)
            frecuencia[inde] += 1
    return clase,frecuencia
        