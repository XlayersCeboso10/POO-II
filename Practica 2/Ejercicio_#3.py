class Precios:
    PV = float(input("Ingresa el precio de venta: "))

    def Precio_de_produccion(self):
       
        self.Precio_venta = (self.PV * 1.2)
        print (f"El precio de producción es {self.Precio_venta}")

    def IVA(self):
        self.iva = (self.PV * 0.16)
        print (f"El valor del IVA es {self.iva}%")

    def Precio_total(self):
        Precioo = (self.iva + self.PV + self.Precio_venta)
        print(f"El preciofinal es {Precioo} ")
        

Objeto = Precios()
Objeto.IVA()
Objeto.Precio_de_produccion()
Objeto.Precio_total()
