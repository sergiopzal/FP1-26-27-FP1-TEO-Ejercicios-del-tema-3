from cadenas import estiliza_mensaje
  
def test_estiliza_mensaje():
    print("Probando estiliza_mensaje...")
    assert estiliza_mensaje("Fundamentos de programación 1") == "FuNdAmEnToS dE pRoGrAmAcIóN 1"
    assert estiliza_mensaje("Murciélago", usa_dieresis=True) == "MüRcÏéLäGö"
    assert estiliza_mensaje("Soy un programador experto", sustituye_espacios="*") == "SoY*uN*pRoGrAmAdOr*ExPeRtO"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=False, usa_dieresis=True, sustituye_espacios="-") == "Hölä-Mündö"
    assert estiliza_mensaje("Hola Mundo", alterna_may_min=True, usa_dieresis=False, sustituye_espacios="_") == "HoLa_MuNdO"

test_estiliza_mensaje()
print("Todas las pruebas pasaron correctamente.")

from cadenas import invierte_texto

def test_invierte_texto():
    print('Probando invierte texto...')
    assert invierte_texto("Texto de prueba") == "abeurp ed otxeT"
    assert invierte_texto('seres') == 'seres'


#test_invierte_texto()
#print("Todas las pruebas pasaron correctamente.")

from cadenas import es_palindromo

def test_es_palindromo():
    print('Probando es palindromo:')
    assert es_palindromo('reconocer')
    assert es_palindromo('rotor')
    assert es_palindromo('radar')
    assert es_palindromo('Amor a Roma',True,True)
    assert es_palindromo('Luz azul',True,True)

#test_es_palindromo()
#print('Todas las pruebas pasaron correctamente.')


