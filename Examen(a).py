def ordenar(lista, cant):
   if cant>1:
       for f in range(0, cant -1):
           if lista[f]>lista[f + 1]:
               aux = lista[f]
               lista[f]=lista[f + 1]  
               lista[f + 1] = aux
       ordenar(lista, cant - 1)

datos=[12,11,10,9,8,7,6,5,4,3,2,1]       
print(datos)
ordenar(datos, len(datos))         
print(datos)
