from funciones_actividad_2_BPP import suma, media
import pytest

def test_1_suma(): #Comprobamos que suma correctamente
    [x,y,z] = [3,2,1]
    assert suma([x,y,z]) == 6

def test_2_suma(): #Comprobamos que también acepta números negativos y decimales
    [x,y,z,a] = [3,0.5,-2,5]
    assert suma([x,y,z,a]) == 6.5

def test_1_media(): #Comprobamos que calcula valores medios del vector de entrada
    [x,y,z] = [0,5,10]
    assert media([x,y,z]) == 5

def test_2_media(): #Comprobamos que funciona con decimales
    [x,y] = [5.5, 6.5]
    assert media([x,y]) == 6

def test_3_media(): #Comprobamos que devuelve un número decimal, y no un string o alguna otra clase
    [x,y,z,k] = [4,9,456,3]
    assert type(media([x,y,z,k])) == float