class tarea:
    def _int_(self):
        pass
    def calcularjornada(self):
        ht, he, het =0,0,0
        ph, phe, pt, ph8=0,0,0,0
        ht=int(input("ingrese horas trabajaras: "))
        ph=float(input("ingrese valor hora: "))
        if ht>40:
            he=ht-40
            if he>8:
                het=he-8
                ph8=8*ph*2
                phe=het*ph*3
            else:
                phe=0
                ph8=he*ph*2
            
            pt=40*ph+ph8+phe
        else:
            pt= ht*ph
            print("sobretiempo<8:{} sobretiempo>8:{} jornda: {} ".format(ph8,phe, pt))
            print("El pago total de horas trabajadas es ", pt)
tarea= tarea()
tarea.calcularjornada()
        