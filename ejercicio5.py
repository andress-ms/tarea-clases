class DiaDePago:
    def __init__(self):
        self._nombre_dia = ""

    def obtener_nombre_dia(self):
        return self._nombre_dia

    def establecer_nombre_dia(self, value):
        self._nombre_dia = value

    def es_dia_de_pago(self):
        dia_actual = self._nombre_dia.lower()

        if dia_actual == 'viernes':
            return True
        else:
            return False

dia_ingresado = input("Ingrese el nombre del día de la semana: ")

dia_pago = DiaDePago()
dia_pago.establecer_nombre_dia(dia_ingresado)

print("¿Es día de pago?", dia_pago.es_dia_de_pago())
