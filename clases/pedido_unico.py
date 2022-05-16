#pedido_unico(pu)
class pedido_unico:
    """
    p<= cu/cu+co
    cu = costo de subestimar
    co = costo de sobreestimar
    """
    def __init__(self,cu,co):
        self.cu = cu
        self.co = co
    def pu(self):
        return (self.cu/(self.cu+self.co))
    def qpu(self,x,z,sigma):
        #agregar funcion generar z
        qpu = x + z * sigma
        if type(qpu) == float:
            r = round(qpu) + 1
            return r
        else:
            return qpu 


#Test
tahiris = pedido_unico(0.3,0.20)
po = tahiris.pu()
print(po)
qpu = tahiris.qpu(5,-0.57,3)
print(qpu)