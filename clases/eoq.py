from math import sqrt


class eoq:
    def __init__(self,nsemanas,datos,costo_pieza,costo_pedir,tasa):
        self.nsemanas = nsemanas
        self.datos = datos
        self.costo_pieza = costo_pieza
        self.costo_pedir = costo_pedir
        self.tasa = tasa
    
    def demeoq(self):
        dp = 0
        demq = 0
        for x in self.datos:
            dp += float(x)
        dp *= 52 
        dp /= 8
        demq = sqrt((2*dp*self.costo_pedir) / (self.costo_pieza * ((self.tasa / 100)*52)))
        return  round(demq)


    def eoqtotal(self,inventario): 
        contador = 1
        costo_total = 0
        lisI = list()
        lisH = list()
        lisD = list()
       
        h = inventario
        for y in self.datos:
            if h > y:
                h = h - float(y)
                lisI.append(h)
              
            else:
                h += inventario
                h = h - float(y)
                lisI.append(h)

        for z in range(len(self.datos)):
            cts = (0.5/ 100) * 10 * lisI[z]
            lisH.append(round(cts,2))
        lisD = [inventario]
        lisS = [self.costo_pedir]
        lisCT = [lisH[0]+self.costo_pedir]
        cl=1
        for z in range(len(self.datos)-1):
            if cl > len(self.datos)-1:
                break
            elif lisI[z+1] > self.datos[z+1]:
                lisD.append(0)
                lisS.append(0)
                cl += 1
            else:
                lisD.append(0)
                lisS.append(0)
                cl += 1
                lisD.append(351)
                lisS.append(47)
                cl += 1
        for z in range(len(self.datos)-1):
            if lisS[z+1] != 0:
                lisCT.append(round(lisCT[z]+lisH[z+1]+lisS[z+1],2))
            else:
                lisCT.append(round(lisCT[z]+lisH[z+1],2))
        tabla = {}
        
        for x in self.datos:
            tabla[f"{contador }"] = \
                    { 
                        "semana": contador ,
                        "demanda": x, 
                        "producto": lisD[contador-1],
                        "inventario" : lisI[contador-1], 
                        "h":lisH[contador-1],
                        "costo_pedir": lisS[contador-1], 
                        "costo_total": lisCT[contador-1]                       
                    }
            costo_total += self.costo_pedir
            contador += 1
        return tabla

prueba = eoq(8,[50,60,70,60,95,75,60,55],10,47,0.5)
 

def lista_float(string):
    b = string.split(",")
    return b

inv = prueba.demeoq()
resultado = prueba.eoqtotal(inv)
print(resultado)

"""
datos = [50,60,70,60,95,75,60,55]
inventario = 351
lisI = list()
h = inventario
for y in datos:
            if h > y:
                h = h - float(y)
                lisI.append(h)
              
            else:
                h += inventario
                h = h - float(y)
                lisI.append(h)
print(lisI)
lisH = list()
for z in range(len(datos)):
            cts = (0.5/ 100) * 10 * lisI[z]
            lisH.append(round(cts,2))
print(lisH)

lisD = [inventario]
lisS = [47]
lisCT = [lisH[0]+47]
cl=1
for z in range(len(datos)-1):
    if cl > len(datos)-1:
        break
    elif lisI[z+1] > datos[z+1]:
        lisD.append(0)
        lisS.append(0)
        cl += 1
    else:
        lisD.append(0)
        lisS.append(0)
        cl += 1
        lisD.append(351)
        lisS.append(47)
        cl += 1
   # print(cl)
print(lisD)
print(lisS)

for z in range(len(datos)-1):
    if lisS[z+1] != 0:
        lisCT.append(round(lisCT[z]+lisH[z+1]+lisS[z+1],2))
    else:
        lisCT.append(round(lisCT[z]+lisH[z+1],2))
    print(f"{lisCT[z]}:{lisH[z+1]}")

print(lisCT)
"""