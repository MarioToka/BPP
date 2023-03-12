from funciones_actividad_2_BPP import suma, media
import unittest

class Test_actividad_2(unittest.TestCase):
    def test_1_suma(self): #Comprobamos que suma correctamente
        [x,y,z] = [3,2,1]
        resul = suma([x,y,z])
        self.assertEqual(resul, 6)

    def test_2_suma(self): #Comprobamos que también acepta números negativos y decimales
        [x,y,z,a] = [3,0.5,-2,5]
        resul = suma([x,y,z,a])
        self.assertEqual(resul, 6.5)

    def test_1_media(self): #Comprobamos que calcula valores medios del vector de entrada
        [x,y,z] = [0,5,10]
        resul = media([x,y,z])
        self.assertEqual(resul, 5)

    def test_2_media(self): #Comprobamos que funciona con decimales
        [x,y] = [5.5, 6.5]
        resul = media([x,y])
        self.assertEqual(resul, 6)

    def test_3_media(self): #Comprobamos que devuelve un número decimal, y no un string o alguna otra clase
        [x,y,z,k] = [4,9,456,3]
        self.assertEqual(type(media([x,y,z,k])), float)