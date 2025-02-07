import math

class Calculadora_Temperatura:
    Grados_Fahrenheit = 0

    def IngresarValores(self):
        self.Grados_Fahrenheit = float(input("Ingresa los grados Fahrenheit: "))

    def Fahrenheit_aCelsius(self):
        Celsius = ((self.Grados_Fahrenheit - 32) / 1.8)
        print(f"{self.Grados_Fahrenheit} grados Fahrenheit equivalen a {Celsius} grados Celsius")

    def Fahrenheit_aKelvin(self):
        Kelvin = ((self.Grados_Fahrenheit + 459.67) / 1.8)
        print(f"{self.Grados_Fahrenheit} grados Fahrenheit equivalen a {Kelvin} grados Kelvin")

Objeto = Calculadora_Temperatura()
Objeto.IngresarValores()
Objeto.Fahrenheit_aCelsius()
Objeto.Fahrenheit_aKelvin()
