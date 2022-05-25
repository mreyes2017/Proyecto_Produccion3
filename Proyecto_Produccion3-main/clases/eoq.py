class eoq:
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
        for x in self.datos:
            tabla[f"{contador + 1}"] = \
                    { 
                        "semana": contador + 1,
                        "demanda": x, 
                        "producto": x,
                        "inventario" : 0, 
                        "h":0,
                        "costo_pedir": self.costo_pedir, 
                        "costo_total": costo_total                       
                    }
            costo_total += self.costo_pedir
            contador += 1
        return tabla

prueba = l4l(8,[50,60,70,60,95,75,60,55],10,47,0.05)
 

def lista_float(string):
    b = string.split(",")
    return b

resultado = prueba.ltotal()


#print(resultado[str(1)])


      