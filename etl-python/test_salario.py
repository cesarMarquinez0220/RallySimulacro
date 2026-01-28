import unittest

def calcular_salario_neto(salario_bruto):
    if salario_bruto < 0:
        raise ValueError("El salario no puede ser negativo")
    return salario_bruto * (1 - 0.0975)


# 1. La Lógica que queremos probar (Simulación de tu script de intereses)
def calcular_nuevo_saldo(deuda_actual, tasa_interes):
    if deuda_actual < 0:
        raise ValueError("La deuda no puede ser negativa")
    return deuda_actual * (1 + tasa_interes)

# 2. La Clase de Prueba (Hereda de unittest.TestCase)
class TestNominaLogica(unittest.TestCase):

    def test_calculo_salario_neto_1000(self):
        salario_bruto = 1000
        resultado_esperado = 902.50

        resultado_real = calcular_salario_neto(salario_bruto)

        self.assertAlmostEqual(resultado_real, resultado_esperado, places=2)
# 3. El disparador para correr las pruebas
if __name__ == '__main__':
    unittest.main()