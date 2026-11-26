import unittest
from legibilidad import calcular_legibilidad, clasificar_legibilidad


class PruebasLegibilidad(unittest.TestCase):
    def test_clasificacion_registrada(self):
        self.assertEqual(clasificar_legibilidad(44.64), "Algo difícil")

    def test_limites_inflesz(self):
        self.assertEqual(clasificar_legibilidad(40), "Algo difícil")
        self.assertEqual(clasificar_legibilidad(55), "Normal")
        self.assertEqual(clasificar_legibilidad(65), "Bastante fácil")
        self.assertEqual(clasificar_legibilidad(80), "Muy fácil")

    def test_no_hay_division_entre_cero(self):
        self.assertIsNone(calcular_legibilidad(0, 1, 0))
        self.assertEqual(clasificar_legibilidad(None), "Sin datos suficientes")

    def test_formula(self):
        self.assertEqual(calcular_legibilidad(126, 8, 273), 56.10)
        self.assertEqual(calcular_legibilidad(126, 7, 273), 53.85)


if __name__ == "__main__":
    unittest.main()
