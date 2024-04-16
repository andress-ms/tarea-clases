# Resuelva el siguiente problema: Leer dos números del teclado y multiplicarlos si son iguales, restarlos si el primero es 
# mayor que el segundo o sumarlos si el primero es menor que el segundo. Diseñe la clase con los atributos, métodos y propiedades requeridos

class operar_numeros:
    def __init__(self, numero1, numero2):
        
        self.numero1 = numero1
        self.numero2 = numero2
        self.operacion = self.determinar_operacion()
        self.resultado = self.calcular_resultado()
    
    def determinar_operacion(self):
        
        if self.numero1 == self.numero2:
            return "multiplicar"
        elif self.numero1 > self.numero2:
            return "restar"
        else: 
            return "sumar"
    
    def calcular_resultado(self):
        
        if self.operacion.lower() == "multiplicar":
            return self.numero1 * self.numero2
        elif self.operacion.lower() == "restar":
            return self.numero1 - self.numero2
        else:
            return self.numero1 +self.numero2
    
    def mostrar_resultado(self):
        print(f"El resultado de {self.operacion} {self.numero1} y {self.numero2} es {self.resultado}")
    
def menu():
    while True:
        try:
            numeros = operar_numeros(float(input("Ingrese el primer numero: ")), float(input("Ingrese el segundo numero: ")))
            break
        except ValueError: 
            print("Ingresó un valor inválido, por favor ingrese un número entero. ")
    
    numeros.mostrar_resultado()

menu()