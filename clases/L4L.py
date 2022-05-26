class metodo_l4l():
   def __init__(self,semanas,costo_pedir,costo_articulo,costo_mantenimiento,demanda):
     self.semanas=semanas
     self.costo_pedir=costo_pedir
     self.costo_articulo=costo_articulo
     self.costo_mantenimiento=costo_mantenimiento
     self.demanda=demanda
   
   def imprimir_tabla(self):
     tabla=[[]]
     cont=1
     tabla[0].append(["SEMANA","DEM","PROD","INV","H","S","CT "])
     for i in range(1,self.semanas+1):
         tabla.append([])
         for j in range(2):
           tabla[i].append(cont)
           cont=cont+1
           tabla[1].append(self.demanda[j])
           
     for i in range(0,self.semanas+1):
         for j in range(1):
           print(tabla[i][j],end=' ')
         print()
    # for f in tabla:
     #    print(f)
             


      
    
       
#prueba 
prueba=metodo_l4l(3,47,10,0.05,[[0],[3],[8]])
prueba.imprimir_tabla()






       






      
