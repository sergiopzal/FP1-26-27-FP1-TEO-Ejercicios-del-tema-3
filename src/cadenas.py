def invierte_texto(texto: str):
    texto_inv = ''
    for i in range(len(texto)-1,-1,-1):
        texto_inv = texto_inv + texto[i]
    return texto_inv

#print(invierte_texto('ordenador'))

def es_palindromo(cadena:str,ignora_espacio:bool= False,ignora_mayuscula:bool= False)-> bool:
    if ignora_espacio:
        cadena = cadena.replace(' ','')
    if ignora_mayuscula:
        cadena = cadena.lower()
    resultado = invierte_texto(cadena)

    if resultado == cadena:
        return True
    else:
        return False    

def estiliza_mensaje(cadena:str,alterna_may_min:bool=True,usa_dieresis:bool=False,sustituye_espacios:str=' ')-> str:
    resultado =''
    espacios_o_digitos = 0
    if alterna_may_min:
        for i in range(len(cadena)):
            if cadena[i] == ' ' or cadena[i].isdigit():
                espacios_o_digitos += 1
                resultado += cadena[i] 
            else:
                if (i + espacios_o_digitos) == 0 or (i+espacios_o_digitos)%2 == 0:
                    resultado += cadena[i].upper()
                else:
                    resultado += cadena[i].lower()

    if usa_dieresis:
        vocales = 'aeiouAEIOU'
        remplazo = 'äëïöüÄËÏÖÜ'
        if resultado == '':
            for i in range(len(vocales)):
                cadena = cadena.replace(vocales[i],remplazo[i])
            resultado = cadena
        else:
            for i in range(len(vocales)):
                resultado = resultado.replace(vocales[i],remplazo[i])

    if sustituye_espacios != ' ':
        if resultado == '':
            cadena = cadena.replace(' ',sustituye_espacios)
            resultado = cadena
        else:
            resultado = resultado.replace(' ',sustituye_espacios)

    return resultado