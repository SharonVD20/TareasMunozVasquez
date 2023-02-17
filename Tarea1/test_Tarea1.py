import pytest
import Tarea1 as tarea1
import math

# Se parametriza para no iterar diferentes veces el mismo test
# Esto comprueba resultados y errores de introducción de parámetros diferentes.
operaciones = [("ABcd12$%", 1, ("AB12", "cd$%")), ("ABcd12$%", 2,
               ("ABcd", "12$%")), ("ABcd12$%1", 2, ("ABcd1", "2$%1"))]


@pytest.mark.parametrize("frase, operacion, valor_esperado", operaciones)
def test_tarea1(frase, operacion, valor_esperado):

    # Se utilizan los valores parametrizados para realizar el test.
    assert tarea1.divide_string(frase, operacion) == valor_esperado


def test_tarea2():

    # Se comprueba el error de parámetro frase de tipo diferente a str.
    assert tarea1.divide_string(2, 2) == "E13"


def test_tarea3():

    # Se comprueba el error de parámetro operacion de tipo diferente a int.
    assert tarea1.divide_string("hola", "a") == "E12"


def test_tarea4():

    # Se comprueba el resultado correcto dado por la función.
    assert tarea1.measure_area(2) == (4, math.pi * 4)


def test_tarea5():

    # Se comprueba el error de parámetro de tipo diferente a int.
    assert tarea1.measure_area("a") == "E14"
