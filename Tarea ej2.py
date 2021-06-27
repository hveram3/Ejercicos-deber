class ventas ():
    def calcularcomisiones (self):
        sb,ventas1,ventas2,ventas3,total_de_ventas=0,0,0,0,0
        comision,sueldo_total=0,0
        sb=float(input("ingrese valor del sueldo:"))
        ventas1=float(input("Ingrese valor 1:"))
        ventas2=float(input("Ingrese valor 2:"))
        ventas3=float(input("ingrese valor 3:"))
        
        total_de_ventas=ventas1+ventas2+ventas3
        comision=total_de_ventas*0.10
        sueldo_total=sb+comision
        
        print("Valor del sueldo total es: $",sb)
        print("total_de_ventas es:$",total_de_ventas)
        print("Comision de las ventas:$",comision)
        print("El sueldo total es:$",sueldo_total)
venta=ventas()
venta.calcularcomisiones()
        
                