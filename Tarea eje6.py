# En una tienda se ofrece un descuento del 15%
# sobre el total de la compra y un cliente
# desea saber cuanto debera pagar finalmente por su compra.

class descuento():
    def descuento(self):
        Tc=float(input("Valor de la compra:"))
        D= Tc*0.15
        Cp=Tc-D
        print("Descuento del valor total es:", D)
        print("Cantidad a pagar es:", Cp)
descuento=descuento()
descuento.descuento()