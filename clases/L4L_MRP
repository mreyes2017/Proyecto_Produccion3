
from openpyxl import NUMPY
class Producto:
   def __init__(self,nombre,cantidad,tiempo_pedido):
     self.nombre=nombre
     self.cantidad=cantidad
     self.tiempo_pedido=tiempo_pedido
     #lista_producto=list()

   #metodo get
   def getnombre(self):
        return self.nombre
    #metodo set
   def setnombre(self, nuevonombre):
        self.nombre = nuevonombre
         #metodo get
   def getcantidad(self):
        return self.cantidad
    #metodo set
   def setcantidad(self, nuevacantidad):
        self.nombre = nuevacantidad
         #metodo get
   def gettiempo_pedido(self):
        return self.tiempo_pedido
    #metodo set
   def setnombre(self, nuevotiempo_pedido):
        self.nombre = nuevotiempo_pedido


class metodo_l4l():
   #producto = Producto()
   #listaProductoExistentes = list(producto)

   def __init__(self,semanas,costo_pedir,costo_articulo,costo_mantenimiento):
     self.semanas=semanas
     self.costo_pedir=costo_pedir
     self.costo_articulo=costo_articulo
     self.costo_mantenimiento=costo_mantenimiento
   
   def requerimientos_netos(self):
     indice=0
     demanda=[self.semanas]
     
     for numero in range(0,self.semanas):
       demanda[indice]=input("Ingrese la demanda")
       print(demanda[indice])
       arr = NUMPY.array([["semana", "demanda","producto","Inventario","H","s","ct"]])
       
#ingresando los valores de la tabla
     
     for i in range(1,self.semanas):
      for j in range(0,6):
        arr[i][j]=NUMPY.append(input("Digite el valor="))
      
    
       
#prueba 
prueba=metodo_l4l(5,47,10,0.05)
prueba.requerimientos_netos()






       






      
