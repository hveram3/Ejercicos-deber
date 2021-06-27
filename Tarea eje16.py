#Ejercicio 16: Determinar si un número entero proporcionado por el usuario es primo.
# Un número primo es un entero que no tiene más divisores que él mismo y la unidad. 

class Indentificar:
    def Numentero(self):
        primo= 0
        divisor=2
        num=int(input("Ingresar un numero entero: "))
        while divisor < num and primo ==0 :
            Res= num%divisor
            print(Res)
            if Res == 0:
                primo+=1
            divisor+=1
        if primo ==0:
            print("El número",num,"es primo")
        else:
            print("El número",num,"no es primo")
        print("\n")
        
identificar= Indentificar()
identificar.Numentero()