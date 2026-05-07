
import math


def calcular_area_circulo(radio) :
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo( radio):

    test = True
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return 2 * math.pi * radio

def calcular_area_rectangulo(base,altura):
    if base < 0 or altura < 0:
      raise ValueError("Las dimensiones no pueden ser negativas.")
    return base * altura


def calcular_hipotenusa(a, b):
  
        if a < 0 or b < 0:
            raise ValueError("Los catetos no pueden ser negativos.")
        return math.sqrt(a**2 + b**2)


"""
Aviso para los test de
* calcular_area_circulo()
* calcular_perimetro_circulo()

Para comparar resultados matemáticos con decimales usamos `assertAlmostEqual`.

¿Cómo funciona `assertAlmostEqual`? Comprueba que la diferencia
entre dos números sea lo suficientemente pequeña como para
considerarlos "iguales".

`self.assertAlmostEqual(valor_calculado, valor_esperado, places=N)` donde

* places=N: Indica el número de decimales que queremos que coincidan.

Ejemplos de casos de prueba para los test

* `calcular_area_circulo(1)` => 3.14159...
* `calcular_perimetro_circulo(1)` => 6.283185...
* `calcular_hipotenusa(3, 4)` => 5.0
* `calcular_area_rectangulo(3, 5)` => 15.0 """
