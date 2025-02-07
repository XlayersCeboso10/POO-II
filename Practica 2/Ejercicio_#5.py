import os
os.system('cls')

import math

class Volumen:
    Altura = 0
    Radio = 0

    def IngresarValores(self):
        self.Radio = float(input("Ingresa el valor del Radio: "))
        self.Altura = float(input("Ingresa la longitud de la Altura: "))

    def MostrarValores(self):
        print(f"El valor del Radio ingresado es {self.Radio} y el valor de la Altura es {self.Altura}")

    def CalcularVolumen(self):
        Volumen_Cilindro = (math.pi * self.Radio * self.Radio * self.Altura)
        print(f"El volumen es {Volumen_Cilindro} unidades cúbicas")

Objeto = Volumen()
Objeto.IngresarValores()
Objeto.MostrarValores()
Objeto.CalcularVolumen()