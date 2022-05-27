
class ltc:
    def __init__(self, nsemanas, datos, costo_pieza, costo_pedir, tasa):
        self.nsemanas = nsemanas
        self.datos = datos
        self.costo_pieza = costo_pieza
        self.costo_pedir = costo_pedir
        self.tasa = tasa

    def ltotal(self):
        tabla = {}
        contador = 0

        lisH = list()
        lisproduccion = list()
        lisD = list()
        p = 0
        listc = list()
        for x in self.datos:
            p += float(x)
            lisproduccion.append(float(p))
            dem = float(x)
            lisD.append(float(x))
            listc.append(contador+1)
            listH2 = list()
            listh3 = list()
            listh4 = list()
            contador = 0
            listotal = list()

       # print(lisD)
        # print(lisproduccion)
        l = 0
        for i in range(1, len(self.datos)):
            contador = 0
            lisH.append(lisproduccion[i]-lisD[l])
            n = 1
        for i in range(2, len(self.datos)-n):
            contador = 1
            listH2.append(lisH[i]-lisD[contador])

        for element in listH2:
            contador = 2
            listh3.append(element-lisD[contador])

        for e in listh3:
            contador = 3
            listh4.append(e-lisD[contador])

        for i in range(len(self.datos)):
            if(i == 0):
                listotal.append(0)
            if(i == 1):
                listotal.append((lisH[i-1])*(self.costo_pieza*self.tasa))
            if(i == 2):
                listotal.append((lisH[i-1])*(self.costo_pieza*self.tasa) +
                                ((listH2[i-1]-listh3[i-1])*self.costo_pieza*self.tasa))
            if(i == 3):
                listotal.append((lisH[i-1]*(self.costo_pieza*self.tasa))+((listH2[i-3])*(
                    self.costo_pieza*self.tasa))+((listh3[i-3])*(self.costo_pieza*self.tasa)))
            if(i == 4):
                listotal.append((lisH[i-1]*(self.costo_pieza*self.tasa))+((listH2[i-2])*(
                    self.costo_pieza*self.tasa))+((listh3[i-3])*(self.costo_pieza*self.tasa)))
            if(i == 5):
                listotal.append((lisH[i-1]*(self.costo_pieza*self.tasa))+((listH2[i-3])*(self.costo_pieza*self.tasa))+(
                    (listh3[i-3])*(self.costo_pieza*self.tasa))+((listh4[i-3])*(self.costo_pieza*self.tasa)))
            if(i == 6):
                listotal.append((lisH[i-1]*(self.costo_pieza*self.tasa))+((listH2[i-3])*(self.costo_pieza*self.tasa))+(
                    (listh3[i-3])*(self.costo_pieza*self.tasa))+((listh4[i-3])*(self.costo_pieza*self.tasa)))
            if(i == 7):
                listotal.append((lisH[i-1]*(self.costo_pieza*self.tasa))+((listH2[i-3])*(self.costo_pieza*self.tasa))+(
                    (listh3[i-3])*(self.costo_pieza*self.tasa))+((listh4[i-3])*(self.costo_pieza*self.tasa)))

        print(lisH)  # bien primera resta
        print(listH2)  # segunda resta bien
        print(listh3)
        print(listh4)
        print(listotal)
        print(listh4[4])
        costo_total = 47
        cont = 1

        costo_total = self.costo_pedir
        dem =0
        t=0
        v=1
        o=0
        l=0
        z=0
        h=2

        for x in self.datos:
            dem += float(x)
            costo_total = self.costo_pedir+((listotal[cont-1])/1000)

            tabla[f"{cont}"] = \
                {
                "semana": cont,
                "demanda": x,
                "calculo del lote": '1-'+f"{cont}",
                "producto": lisproduccion[cont-1],
                "h": (listotal[cont-1])/1000,
                "costo_pedir": self.costo_pedir,
                "costo_total": costo_total
            }

            

            
            cont += 1

        return tabla

       # print(tabla[str()]["demanda"])
prueba = ltc(8, [50, 60, 70, 60, 95, 75, 60, 55], 10, 47, 0.005)


def lista_float(string):
    b = string.split(",")
    return b


resultado = prueba.ltotal()
