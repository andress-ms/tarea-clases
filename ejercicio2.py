"""2. Implementar la clase operaciones. Se deben ingresar los dos valores enteros, calcular su suma, resta,
 multiplicación y división, cada una en un método, e imprimir dichos resultados."""

class Operaciones:
    def __init__ (self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
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
        
valor1 = int(input("Ingrese el primer entero: "))
valor2 = int(input("Ingrese el segundo entero: "))

operaciones = Operaciones(valor1, valor2)

print("Suma:", operaciones.suma())
print("Resta:", operaciones.resta())
print("Multiplicacion:", operaciones.multiplicacion)
print("Division:", operaciones.division)

