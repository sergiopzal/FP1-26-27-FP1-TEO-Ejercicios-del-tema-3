from eventos import *

def test_es_dia_no_laborable():
    assert(es_dia_no_laborable(date.today())) == False
    assert(es_dia_no_laborable(date(2026,10,11))) == True
    assert(es_dia_no_laborable(date(2026,10,10))) == True
    assert(es_dia_no_laborable(date(2026,10,12))) == True


def test_calcula_siguiente_valida():
    assert calcular_siguiente_valida(date(2026,10,13),1) == date(2026,10,14)
    assert calcular_siguiente_valida(date(2026,10,9),2) == date(2026,10,13)

test_es_dia_no_laborable()
test_es_dia_no_laborable()
planificar_eventos(date(2026, 1, 1),10,5)
print('Todos los test pasaron correctamente.')

