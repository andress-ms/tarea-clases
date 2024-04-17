"""2. Implementar la clase operaciones. Se deben ingresar los dos valores enteros, calcular su suma, resta,
 multiplicación y división, cada una en un método, e imprimir dichos resultados."""

class Operaciones:
    def __init__(self, valor1, valor2):
        if isinstance(valor1, int) and isinstance(valor2, int):
            self.valor1 = valor1
            self.valor2 = valor2
        else:
            raise ValueError("Los valores deben ser enteros.")

    def suma(self):
        return self.valor1 + self.valor2

    def resta(self):
        return self.valor1 - self.valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            print("No se puede dividir entre cero.")
            return None

try:
    valor1 = int(input("Ingrese el primer número entero: "))
    valor2 = int(input("Ingrese el segundo número entero: "))

    operaciones = Operaciones(valor1, valor2)

    print("Suma:", operaciones.suma())
    print("Resta:", operaciones.resta())
    print("Multiplicación:", operaciones.multiplicacion())
    print("División:", operaciones.division())

except ValueError:
    print("Error: Debes ingresar números enteros.")

