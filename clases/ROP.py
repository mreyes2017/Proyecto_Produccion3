from math import sqrt
class ROP:
    def __init__(self,demanda,plazo_entrega,tipo):
        self.demanda = demanda
        self.plazo_entrega = plazo_entrega
        self.tipo=tipo
        

    def calcular_rop(self):
        if self.tipo==360:
         demanda_por_dia = float(self.demanda / 360)
         rop = round(float(demanda_por_dia*self.plazo_entrega),2) 
         return rop 
        elif self.tipo==30:
         demanda_por_dia = float(self.demanda / 30)
         rop = round(float(demanda_por_dia*self.plazo_entrega),2) 
         return rop 
        elif self.tipo==6:
         demanda_por_dia = float(self.demanda / 6)
         rop = round(float(demanda_por_dia*self.plazo_entrega),2) 
         return rop 
        else:
         demanda_por_dia = float(self.demanda)
         rop = round(float(demanda_por_dia*self.plazo_entrega),2) 
        return rop 

#prueba xd

#rop_p = ROP(1500000,360,2)
#ROP=rop_p.calcular_rop()




