# Leer tres numeros enteros diferentes entre si y determinar el numero mayor de los tres
class numero_mayor():
    def numeroenteromayor (self):
        n1=int(input("Escriba numero1: "))
        n2=int(input("Escriba numero2: "))
        n3=int(input("Escriba numero3:"))
        if n1 > n2 and n1 > n3:
            print("El numero mayor es: ", n1)
        elif n2 > n1 and n2 > n3:
            print("El numero mayor es: ", n2)
        else:
            print("El numero mayor es: ",n3)
        
numero=numero_mayor()
numero.numeroenteromayor()