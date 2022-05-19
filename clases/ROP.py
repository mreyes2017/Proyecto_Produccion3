from math import sqrt
class ROP:
    def __init__(self,demanda,plazo_entrega):
        self.demanda = demanda
        self.plazo_entrega = plazo_entrega
        

    def calcular_rop(self):
        demanda_por_dia = float(self.demanda / 360)
        rop = round(float(demanda_por_dia*self.plazo_entrega),2) 
        return rop 


#prueba xd

#rop_p = ROP(1500000,360,2)
#ROP=rop_p.calcular_rop()

#punto de reorden con desviacion estandar

class ROP_ESTANDAR:
    def __init__(self,demanda_por_dia,plazo_entrega,z,desviacion):
        self.demanda_por_dia= demanda_por_dia
        self.plazo_entrega= plazo_entrega
        self.desviacion=desviacion
        self.z=z

    def calcular_desviacion(self):
        Rl= self.desviacion*sqrt(self.plazo_entrega)
        rop_estandar= float(self.demanda_por_dia*self.plazo_entrega)+(self.z*Rl)
        return round(rop_estandar,2)
#prueba x2

rop_estandar=ROP_ESTANDAR(200,4,1.65,150)
ROP_ESTANDAR= rop_estandar.calcular_desviacion()

