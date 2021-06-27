# Calcular la suma de los cuadrados de los primeros 100
# entreros y escribir el resultado

class numero():
    def numeroscuadrados(self):
        num,sum=0,0
        num=int(input("Limite de cuadrados:"))
        print()
        for i in range(1,num+1):
          print(i,"^2")
          print("+")
          sum=sum+(i*2)
          print("La suma de los cuadrados es:",sum)

numero=numero()
numero.numeroscuadrados()