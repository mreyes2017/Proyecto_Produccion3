from math import sqrt
from math import *

class qr:
    def __init__(self,demanda,costo_pedir,costo_almacen,costo_compra,tipo):
        self.demanda = demanda
        self.costo_pedir = costo_pedir
        self.costo_almacen = costo_almacen
        self.costo_compra = costo_compra
        self.tipo=tipo

    def calcular_q(self):
       if self.tipo==360:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         q = sqrt((2*float(self.demanda) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
         return round(q,2) 
       elif self.tipo==30:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         q = sqrt((2*float(self.demanda*12) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
         return round(q,2) 
       elif self.tipo==6:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         q = sqrt((2*float(self.demanda*48) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
         return round(q,2) 
       else :
         costo_almacen_decimal = float(self.costo_almacen / 100)
         q = sqrt((2*float(self.demanda*360) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
         return round(q,2) 


class n_pedidos:
    def __init__(self,demanda,q,tipo):
        self.demanda = demanda
        self.q = q
        self.tipo=tipo
    
    def calcula_n_pedidos(self):
        if self.tipo==360:
         return (self.demanda / self.q)
        elif self.tipo==30:
         return ((self.demanda*12) / self.q)
        elif self.tipo==6:
         return ((self.demanda*48) / self.q)
        else:
         return ((self.demanda*360) / self.q)


class tiempo_entre_pedidos:
    def __init__(self,dias,pedido):
        self.pedido = pedido
        self.dias = dias
        
    
    def tiempo_entre_pedido(self):
        tiempo = float(self.dias / self.pedido)
        return tiempo

class costo_total:
    """
        CT = Ds/Q + Q.H/2 +DC
    """
    def __init__(self,demanda,costo_pedir,costo_almacen,costo_compra,q,tipo):
        self.demanda = demanda
        self.costo_pedir = costo_pedir
        self.costo_almacen = costo_almacen
        self.costo_compra = costo_compra
        self.q = q
        self.tipo=tipo

    def c_total(self):
        if self.tipo==360:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         return ((self.demanda * self.costo_pedir)/ self.q) + ((self.q * costo_almacen_decimal * self.costo_compra) / 2 )+ (self.demanda * self.costo_compra)
        elif self.tipo==30:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         return (((self.demanda*12) * self.costo_pedir)/ self.q) + ((self.q * costo_almacen_decimal * self.costo_compra) / 2 )+ (self.demanda * self.costo_compra)
        elif self.tipo==6:
         costo_almacen_decimal = float(self.costo_almacen / 100)
         return (((self.demanda*48) * self.costo_pedir)/ self.q) + ((self.q * costo_almacen_decimal * self.costo_compra) / 2 )+ (self.demanda * self.costo_compra)
        else :
         costo_almacen_decimal = float(self.costo_almacen / 100)
         return (((self.demanda*360) * self.costo_pedir)/ self.q) + ((self.q * costo_almacen_decimal * self.costo_compra) / 2 )+ (self.demanda * self.costo_compra)
