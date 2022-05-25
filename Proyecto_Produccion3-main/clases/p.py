from cmath import sqrt
from statistics import NormalDist
from math import *
class pr:
    def __init__(self,demanda,desviacion,periodo,plazo,inventario,nivel):
        self.demanda = demanda
        self.desviacion=desviacion
        self.periodo=periodo
        self.plazo=plazo
        self.inventario=inventario
        self.nivel=nivel
    
    def calcular_z(self):
     self.z = round(NormalDist().inv_cdf(((self.nivel)/100)),4)
     return self.z
     
    def calcular_p(self):
     x = round(((float(self.demanda)*(float(self.periodo+self.plazo)))+(float(self.z)*(float(self.desviacion)*sqrt(float(self.periodo)+float(self.plazo))))-float(self.inventario)))
     return x

    def inventario_seguridad(self):
     ss = round(float(self.z)*(float(self.desviacion)*sqrt(float(self.periodo)+float(self.plazo))))
     return ss


#prueba z
s = pr(10,3,30,14,150,98)
o = s.calcular_z()
k = s.calcular_p()
l = s.inventario_seguridad()
print(o)
print(k)
print(l)