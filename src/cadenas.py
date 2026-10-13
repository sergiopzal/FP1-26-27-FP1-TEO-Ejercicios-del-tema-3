def invierte_texto(texto: str)-> str:
    '''Invierte el texto que recibe por paramentro'''
    texto_inv = ''
    for i in texto:
        texto_inv = i + texto_inv
    return texto_inv

print(invierte_texto('ordenador'))

def es_palindromo(cadena:str,ignora_espacio:bool= False,ignora_mayuscula:bool= False)-> bool:
    if ignora_espacio:
        cadena = cadena.replace(' ','')
    if ignora_mayuscula:
        cadena = cadena.lower()
    res = invierte_texto(cadena)

    return res == cadena  

def estiliza_mensaje(cadena:str,alterna_may_min:bool=True,usa_dieresis:bool=False,sustituye_espacios:str=' ')-> str:
    res =''
    espacios_o_digitos = 0
    if alterna_may_min:
        for i in range(len(cadena)):
            if cadena[i] == ' ' or cadena[i].isdigit():
                espacios_o_digitos += 1
                res += cadena[i] 
            else:
                if (i + espacios_o_digitos) == 0 or (i+espacios_o_digitos)%2 == 0:
                    res += cadena[i].upper()
                else:
                    res += cadena[i].lower()

    if usa_dieresis:
        vocales = 'aeiouAEIOU'
        remplazo = 'äëïöüÄËÏÖÜ'
        if res == '':
            for i in range(len(vocales)):
                cadena = cadena.replace(vocales[i],remplazo[i])
            res = cadena
        else:
            for i in range(len(vocales)):
                res = res.replace(vocales[i],remplazo[i])

    if sustituye_espacios != ' ':
        if res == '':
            cadena = cadena.replace(' ',sustituye_espacios)
            res = cadena
        else:
            res = res.replace(' ',sustituye_espacios)

    return res