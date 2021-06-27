class Tarea:
    def _init_(self):
        pass
    def CalcularJornada(self):
    
        ht,he,het=0,0,0
        ph,phe,pt,ph8=0,0,0,0
        print("_____________")
        ht=int(input("Ingrese Horas Trabajadas: "))
        ph=float(input("ingrese valor por horas: "))
        if ht > 40:
            he=ht-40
            if he > 8:
                het=he-8
                ph8=8*ph*2
                phe=het*ph*3
            else:
                ph8=he*ph*2
            pt=40*ph+ph8+phe
        else:
            pt= ht*ph
            print()  
        print("Sobretiempo <8 :{} Sobretiempo >8: {} El pago total de horas trabajadas es:$ {}".format(ph8,phe,pt))
       
tarea= Tarea()
tarea.CalcularJornada()