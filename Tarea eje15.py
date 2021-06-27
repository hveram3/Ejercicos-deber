class eje15:
    def __init__(self):
        pass
    def variable (self):
        l=1
        n=int(input("Ingrese un numero para la serie:"))
        s=5
        ser=0
        for a in range (l,n+1):
            s=s+5
            ser=ser+s
        print("Suma de serie es:",ser)
        
resultado= eje15()
resultado.variable()