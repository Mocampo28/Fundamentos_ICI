def Prob1(a):
    mens="hola"
    Menssaj= mens + " "  + a
    return Menssaj

def nomed(nom,edad):
    msj =("Hola " , nom , " tienes " , edad , " años " )

    return msj

def añoNacimiento(aoa,aon):
    return aoa-aon

if __name__ == '__main__':

    #print("Ingresa tu nombre")
    #a=input()
    #print(Prob1(a))


    #print("Ingresa tu Nombre")
    #nom = input()
    #print("Ingresa tu edad")
    #edad=input()
    #print(nomed(nom,edad))


    print("Ingresa tu nombre")
    nom = input()
    print("Ingresa el año actual")
    aoa = input()
    print("Ingresa el año de tu nacimiento")
    aon = input()
    print("Hola" + nom + "Tienes" + añoNacimiento(aoa,aon) + "años")
    
    
def funcion3(a: int, b: int, c: str) -> str:  # Asignar como valores de entrada a y b cuyo tipo de dato seran de tipo integer(int) y c será de tipo string(str) y el valor de salida será tipo string(str)
    edad = a - b
    return funcion2(c, edad)
  
if __name__ == "__main__":
    print("Escribir una funcion que reciba un mensaje y un nombre  escriba en pantalla '<mensaje> <nombre>'")
    print(funcion1("Hola", "Marco")) 
    
    
    print("Escribir una funcion que reciba el nombre y la edad de una persona. EL mensaje de saluda tiene que ser: 'Hola <nombre> tienes <edad> años'")
    print(funcion2("Marco", 20)) 
    
    
    print("Escribir una funcion que recibe el año actual y el año de nacimiento, usando la funcion anterior enviando esta como argumento obtenga el mensaje: 'Hola <nombre> tienes <edad> años'")
    print(funcion3(2022, 2002, "Marco"))
    
