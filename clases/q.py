from math import sqrt


class q:
    def __init__(self,demanda,costo_pedir,costo_almacen,costo_compra):
        self.demanda = demanda
        self.costo_pedir = costo_pedir
        self.costo_almacen = costo_almacen
        self.costo_compra = costo_compra

    def calcular_q(self):
        costo_almacen_decimal = float(self.costo_almacen / 100)
        q = sqrt((2*float(self.demanda) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
        return q


class n_pedidos:
    def __init__(self,demanda,q):
        self.demanda = demanda
        self.q = q
    
    def calcula_n_pedidos(self):
        return (self.demanda / self.q)

class tiempo_entre_pedidos:
    def __init__(self,pedido):
        self.pedido = pedido
    
    def tiempo_entre_pedido(self):
        dias = 360
        tiempo = float(dias / self.pedido)
        return tiempo


#Prueba
william = q(1500000,80,10,2.5)
q = william.calcular_q()
print(q)


moises = n_pedidos(1500000,q)
np = moises.calcula_n_pedidos()
print(np)

oscar = tiempo_entre_pedidos(np)
tp = oscar.tiempo_entre_pedido()
print(tp)