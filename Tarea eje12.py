class variable():
    def variable_entero(self):
        
        num=int(input("Variable 1:"))
        v= int(input("Varible 2:"))
        if num== 1:
            Respt=100*v
        elif num==2:
            Respt=pow(100,v)
        elif num==3:
            Respt=100/v
        else:
            Respt=0
        print("Su Resultado es:", Respt)
        
variable=variable()
variable.variable_entero()