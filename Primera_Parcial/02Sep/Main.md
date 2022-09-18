# Codigo Escrito y visto en la clase del 02 de sept de 2022  

from cmath import e  #En estos codigos importamos librerias que hicimos nosotros mismos  

from re import T #importamos solo una funcion de esa libreria  

from this import d #algunas lineas como estas hacen referencia a codigo en especifico  

from traceback import print_tb  

  
  
Aqui comienza el programa  

if __name__ == "__main__": 

    numerobig= 123141241352313512532131
    print(f"{numerobig:,d}")  
    
    #fijar cantidad de decimales
    numerpi=3.14151321124125412
    print(f"{numerpi:e}")
    print(f"{numerpi:.2e}")
    
    #porcentaje
    porci= 0.431241
    print(f"{porci:%}")
    print(f"{porci:.2%}")
    
    #numeros binarios
    print(f"{25:b}")
    
    #unicodes
    print(f"{13:c}")
    
    #escriba una funcion que genere una tabla de multiplicar recibiendo
    #como argumento la cantidad de numeros y la tabla a generar
    
    
def multi(n:int,t:int):  #definimos una funcion
    
    for i in range(1,n+1):
        print(i,"x", t ,"=" ,i*t )     #cuando no retorna nada se retorna un none   
    return None


    
if __name__ == "__main__":
    
    ntab =input("Ingresa la cantidad de tablas que quieres hacer. ") #codigo extra que quise practicar
    
    

