#Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene un aumento 
# del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class sueldo():
    def sueldo_Aumento(self):
        sue=float(input("Ingrese Sueldo: "))
        if sue>600:
            aum=sue*0.10
            sue=sue+aum
            print("Obtiene aumento:",sue)
        else:
            print("No obtiene aumento")
            print("El sueldo es: ",sue)
sueldo=sueldo()
sueldo.sueldo_Aumento()