class serie():
    def numentero(self):
        
        serie=0
        p=1
        num=int(input("Ingrese un numero entero: "))
        bandera = True
        while p<=num:
            if bandera==True:
                serie = serie+1/p
                bandera = False
            else:
                serie = serie-1/p
                bandera = True
            p=p+1
            print("La suma de la serie es: ",serie)
serie=serie()
serie.numentero()