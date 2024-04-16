# Diseñe una clase y cree un objeto que tenga un atributo 
# (con su respectiva propiedad) para capturar un número entero y 
# determinar si es positivo, negativo o cero. Implementar un método (función) 
# que devuelva el mensaje correspondiente.

class numero_entero:
    
    def __init__(self, numero):
        self.numero = numero
        self.tipo = self.determinar_tipo(numero)
    
    def determinar_tipo(self, numero):
        if self.numero > 0:
            return "positivo"
        elif self.numero < 0:
            return "negativo"
        else:
            return "cero"
    
    def devolver_mensaje(self):
        print(f"El numero es {self.tipo}.")
        
def menu():
    while True:
        try:
            numero = numero_entero(int(input("Ingrese un numero entero: ")))
            break
        except ValueError: 
            print("Ingresó un valor inválido, por favor ingrese un número entero. ")
    
    numero.devolver_mensaje()
    
menu()
    
        
    

