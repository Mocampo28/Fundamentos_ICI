# lista1 = [1,2,3,4,5,6,7,8,9,10]
# N=len(lista1)    #Funcion len es una funcion que cuenta las listas
# print(lista1)
# #print(N)
# #lista2=[1,"asda",1.121,True,False,(1,4,21,1)]
# #print(lista2)


# lista_cal=[]
# #print(lista_cal)

# for i in range(1,N):
#     lista_cal.append(lista1[i])   #For que graba en lista_cal los numeros de otra lista
    
# print(lista_cal)
# #Las listas se manejan en numeros negativos, porque se van recorriendo hacia ese sentido.
# for i in range(1,11):
#     lista_cal.append(i)    #for que graba en la lista_cal los numeros del 1-10
    
# print(lista_cal)


#slices : se dividen en dos partes

# lista=[1,2,3,4,5,6,7,8,9,10]

# print(lista[int(len(lista)/2):]) #calcula cual es la mitad e imprime de la mitad hacia adelante   
# print(lista[:int(len(lista)/2)]) #calcula cual es la mitad e imprime pero la mitad de atras
# print(lista[3:7])    #imprime los numeros del 4-7
# print(lista[-7:-3])  #hace lo mismo que el de arriba pero con indice negativo


# lista1 =[1,"dos",3,"cuatro"]
# print(lista1)
# lista1[1]=2   #cambiamos un valor a lista 1
# print(lista1)
# lista2=lista1  #asignamos el valor de lista 1 a lista 2 y ya tenemos 2 listas iguales "IGUALE"

# lista2=lista1[:]  #asignamos todos los valores de lista 1 y asi obtenemos 2 listas diferentes pero con valores iguales



lista1=[1,2,3,4]
# print(lista1)

# for i in range(5,8):
    
#     lista1.append(i)        #for que agrega "5,6,7" a la lista
#     print(lista1) 
                                

# lista1[5:] = [5,6,7]     #hace lo mismo que el for pero mas rapido
# #tambien se puede usar al revez para agregar valores al inicio
# lista2=[5,6,7]
# print(lista1)   
# lista1[4:5]= [0]
# print(lista1)

# lista1.extend(lista2)  #junta dos listas pero solo los datos

del (lista1[0])  #borrar un elemento en especifico
print(lista1)

del(lista1[0:2])  #borra de un punto hasta otro punto
