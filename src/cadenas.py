def invierte_texto(texto: str):
    texto_inv = ''
    for i in range(len(texto)-1,-1,-1):
        texto_inv = texto_inv + texto[i]
    return texto_inv

print(invierte_texto('ordenador'))