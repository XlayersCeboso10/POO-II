from enum import Enum
from datetime import datetime

class Habitacion(Enum):
    INDIVIDUAL = 1
    DOBLE = 2
    SUITE = 3
import os
os.system('cls')
class Hotel_reservaciones:
    def __init__(self):
        self.Numero_habitacion = int(input("Por favor ingresa el número de habitación: "))
        print("Escoje el tipo de habitación: ")

        for Tipo_de_habitacion in Habitacion:
            print(f"{Tipo_de_habitacion.value}. {Tipo_de_habitacion.name}")
        Tipo_de_habitacion_seleccionado = int(input("Ingresa el numero de habitación segun la etiqueta correspondiente: "))
        self.Tipo_de_habitacion = Habitacion(Tipo_de_habitacion_seleccionado)
        
        self.fecha_checkin = datetime.strptime(input("Ingresa la fecha de ingreso (YYYY-MM-DD): "), "%Y-%m-%d")
        self.fecha_checkout = datetime.strptime(input("Ingresa la fecha de salida (YYYY-MM-DD): "), "%Y-%m-%d")
        self.Cliente = input("Por favor ingresa el nombre del cliente: ")

    def Calcular_dias(self):
        return (self.fecha_checkout - self.fecha_checkin).days

    def Mostrar_info(self):
        print("\n------------- Este es el ticket de la venta -------------")
        print(f"Nombre del cliente: {self.Cliente}")
        print(f"Numero de habitación: {self.Numero_habitacion}")
        print(f"Fecha de ingreso: {self.fecha_checkin.strftime('%Y-%m-%d')}")
        print(f"Fecha de salida: {self.fecha_checkout.strftime('%Y-%m-%d')}")
        print(f"Total de días en el hotel: {self.Calcular_dias()}")
        print(f"Tipo de habitación: {self.Tipo_de_habitacion.name}")

Objeto = Hotel_reservaciones()
Objeto.Mostrar_info()
