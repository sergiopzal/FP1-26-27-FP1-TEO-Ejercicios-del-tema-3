alfabeto = 'abcdefghijklmnñopqrstuvwxyzáéíóúüABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚÜ'
def letra_a_posicion(letra):
    if letra in alfabeto:
        posicion = alfabeto.find(letra)
        return posicion
    else:
        return None
#print(letra_a_posicion('e'))    
def posicion_a_letra(posicion):
    if posicion in range(len(alfabeto)):
        letra = alfabeto[posicion]
        return letra
    else:
        return None
#print(posicion_a_letra(4))
def cifra_cesar(texto:str, clave:int):
    mensaje = ''
    for l in texto:
        if l in alfabeto:
            indice = (letra_a_posicion(l)+clave)
            if indice >= len(alfabeto):
                indice = indice % len(alfabeto)
            mensaje += alfabeto[indice]
        else:
            mensaje += l
    return mensaje
#print(cifra_cesar('Téxn YBzpé',-13))

def rompe_cesar(texto_c):
    for i in range(len(alfabeto)):
        print(f'{i}:',cifra_cesar(texto_c,-i))

print(rompe_cesar('j YÁXOÁJUJÁ ÉN JYÁNVMN yáxoájujvmx!'))
        