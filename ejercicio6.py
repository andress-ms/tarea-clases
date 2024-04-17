cuentas = []

class cuenta_bancaria:
    def __init__(self, nombre, saldo ):
            self.nombre = nombre
            self.numero_cuenta = self.generar_numero_cuenta()
            self.saldo = saldo
        
    def generar_numero_cuenta():
        cantidad_cuentas = len(cuentas) + 1
        return str(cantidad_cuentas).zfill(8)
    
    def actualizar_saldo(self, monto):
        self.saldo += monto

def mostrar_cuentas():
    print("\nLista de cuentas:")
    for cuenta in cuentas:
        print(f"Nombre: {cuenta.nombre}, Número de cuenta: {cuenta.numero_cuenta}, Saldo: {cuenta.saldo}")

def menu():
    while True:
        nombre = input("\nIngresa el nombre del depositante ('Fin' para terminar): ")
        if nombre.upper() == "FIN":
            break
        while True:
            try:
                saldo = float(input("Ingrese el saldo de la cuenta: "))
                if saldo < 0:
                    print("El saldo no puede ser negativo. Intente nuevamente.")
                    continue
                cuentas.append(cuenta_bancaria(nombre, saldo))
                break  # Rompe el bucle mientras si todo está bien
            except ValueError:
                print("Ingresó un valor inválido, por favor ingrese un número.")
    mostrar_cuentas()
    
def buscar_cuenta(numero_buscado):
        for cuenta in cuentas:
            if cuenta.numero_cuenta == numero_buscado:
                return cuenta
        return None
    
def movimiento_cuentas():
    respuesta= input("\n¿Desea realizar un movimiento en la cuenta?\nEscriba 'Si' para continuar: ")
    if respuesta.upper() != "SI":
        return
    cuenta_buscada = input("\nIngrese el numero de cuenta en la que quiere hacer un movimiento: ")
    cuenta_encontrada = buscar_cuenta(cuenta_buscada)
    if cuenta_encontrada:
        movimiento = input("\nEscriba '1' para hacer un deposito o escriba '2' para hacer un retiro")
        if movimiento not in ['1', '2']:
            print("\nNo ingresó una opcion valida")
        else:
            cantidad = float(input("Ingrese el monto del movimiento: "))
            if movimiento == '2':
                if cantidad > cuenta_encontrada.saldo:
                    cantidad *= -1
            cuenta_encontrada.mover_saldo(cantidad)
            print(f"\nMovimiento realizado con exito, nuevo saldo: {cuenta_encontrada.saldo}")    
    else:
        print("\nLa cuenta no fue encontrada.")  

menu()
movimiento_cuentas()