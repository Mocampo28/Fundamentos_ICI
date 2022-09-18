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
