import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3 
    
    def lado1(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El lado debe ser un número.")
        if value <= 0:
            raise ValueError("El lado debe ser positivo.")
        self._lado1 = value


    def lado2(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El lado debe ser un número.")
        if value <= 0:
            raise ValueError("El lado debe ser positivo.")
        self._lado2 = value

   
    def lado3(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("El lado debe ser un número.")
        if value <= 0:
            raise ValueError("El lado debe ser positivo.")
        self._lado3 = value

    def ingresar_valor(self):
        self.lado1 = float(input("Ingrese el valor del lado 1: "))
        self.lado2 = float(input("Ingrese el valor del lado 2: "))
        self.lado3 = float(input("Ingrese el valor del lado 3: "))
    
    def imprimir_area(self):
        s = ((self.lado1 + self.lado2 + self.lado3)/2)
        area = round(math.sqrt(s*(s-self.lado1)*(s-self.lado2)*(s-self.lado3)), 5)

        print (f"El area del triangulo es {area}")

    def tipo_de_triangulo(self):
        if  self.lado1 == self.lado2 == self.lado3:
            print("Es un triangulo equilátero")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado3 == self.lado1:
            print("Es un triangulo isósceles.")
        else:
            print("Es un triangulo escaleno.")
        
triangulo = Triangulo(0, 0, 0)

triangulo.ingresar_valor()
triangulo.imprimir_area()
triangulo.tipo_de_triangulo()
