from asyncio.windows_events import INFINITE
from math import sqrt
from statistics import NormalDist

class pr:
    def __init__(self,demanda,desviacion,periodo,plazo,inventario):
        self.demanda = demanda
        self.desviacion=desviacion
        self.periodo=periodo
        self.plazo=plazo
        self.inventario=inventario

    def calcular_p(self):
        #costo_almacen_decimal = float(self.costo_almacen / 100)
      #  q = sqrt((2*float(self.demanda) * float(self.costo_pedir)) / (float(costo_almacen_decimal) * float(self.costo_compra)))
     #   return  s=NormalDist(mu=10, sigma=19.89)
     # sigma = math.sqrt((p*(1-p))/(n))
      z = round((10 - 19.89) / float(self.desviacion), 2)
      return z

p= pr(5,12,3,5,4)
o=p.calcular_p
print(o)