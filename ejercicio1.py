"""1. Desarrollar un programa que tenga una clase que represente un Cuadrado y tenga los siguientes métodos:
 ingresar valor a su lado, imprimir su perímetro y su superficie."""

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def ingresar_valor_lado(self):
        self.lado = float(input("Ingrese el valor del lado: "))
        if self.lado <= 0:
            raise ValueError("El valor debe ser positivo")

    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    
    def calcular_superficie(self):
        superficie = self.lado ** 2 
        return superficie

Cuadrado1 = Cuadrado(0)

Cuadrado1.ingresar_valor_lado()
print("El valor del perimetro es: ", Cuadrado1.calcular_perimetro())
print("El valor de la superficie es: ", Cuadrado1.calcular_superficie())