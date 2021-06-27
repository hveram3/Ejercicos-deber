class producto():
    
    def suma_producto(self):

        prod=1
        suma=0
        resp=input(str("Desea ingresar numero? (S/N)? : "))
        while resp!="N" and resp!="n":
            num=int(input("Dijite un numero: "))
            suma=suma+num
            prod = prod * num  
            resp=input(str("Desea continuar (S / N)?): "))
        print ("SUMA TOTAL:"  , suma)
        print ("PRODUCTO TOTAL:", prod)    
producto=producto()
     
    