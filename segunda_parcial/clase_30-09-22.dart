void main(){
    Int aact = 2022;
    Int anac = 2002;

    
    print("HOLA ${getnombre()} ${getapel()} TIENES ${edadcalc(aact,anac)} años ")  // $ sirve para concatenar 

}

//funciones
int edadcalc(int aact, int anac){
    return aact-anac;
}

int getnombre(){
    return "Marco";
}

int getapel(){
    return "Ocampo";
}
