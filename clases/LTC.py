class ltc:
    def __init__(self,nsemanas,datos,costo_pieza,costo_pedir,tasa):
        self.nsemanas = nsemanas
        self.datos = datos
        self.costo_pieza = costo_pieza
        self.costo_pedir = costo_pedir
        self.tasa = tasa


    def ltotal(self): 
        tabla = {}
        contador = 0
        costo_total = self.costo_pedir
        dem =0
        t=0
        v=1
        o=0
        l=0
        for x in self.datos:
            dem += float(x)
            tabla[f"{contador + 1}"] = \
                    { 
                        "semana": contador + 1,
                        "demanda": x, 
                        "calculo del lote": '1-'+f"{contador+1}",
                        "producto": dem,
                        "h":l,
                        "costo_pedir": self.costo_pedir, 
                        "costo_total": costo_total                       
                    }
            
            t=((dem-float(x))*(self.costo_pieza)*(self.tasa))
            o=dem-float(x)
            if(o==0):
                l=0
            else:
             z=(o-tabla[f"{contador+1}"]["demanda"])*(self.costo_pieza)*(self.tasa)
             l=t+z
             costo_total = self.costo_pedir+(t/1000)
             contador += 1
             print(tabla[f"{1}"]["demanda"])
             print(l)
        return tabla
        
         
prueba = ltc(8,[50,60,70,60,95,75,60,55],10,47,0.005)
 
def lista_float(string):
 b = string.split(",")
 return b

resultado = prueba.ltotal()


print(resultado[str(1)])


      