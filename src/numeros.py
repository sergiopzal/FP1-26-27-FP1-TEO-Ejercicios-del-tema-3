from cadenas import invierte_texto
def invierte_numero(numero:int)->int:
    resultado = 0
    exp = len(str(numero))
    i = 10
    j = 10**(exp-1)
    if numero > 0:
        while numero > 0:
            resultado += (numero%i)*j
            numero = (numero // i)
            j = j // 10
        return resultado
    else:
        return 0

def convierte_binario(numero:int)->int:
    resultado = ''
    if numero > 0:
        while numero >0:
            resultado += str(numero % 2)
            numero //= 2
        resultado = invierte_texto(resultado)
        return resultado
    else:
        return '0'

