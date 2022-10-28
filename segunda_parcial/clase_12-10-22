void main() {
  // crear una instancia de user
  var usuario1 = user(); // es una instancia(copia) de user
  // user usuario2 = user(); // otra manera de hacer la copia de user

  // print(usuario1.edad); // con el " . " accedemos a las propiedades de la clase}
  // print(usuario2.nombre);

  usuario1.nombre =
      "Marco"; // se pueden asignar valores a las propiedades de la instancia
  usuario1.edad =
      21; // sin embargo no se debe hacer asi, Que se pueda no significa que esta bien
  usuario1.report();

  var clas = estudiante();

  clas.carrera = "Ingenieria en Computacion Inteligente";
  clas.Ncuenta = "20175265";
  clas.Semestre = 3;
  clas.reporrt();
}

//ENCAPSULAMIENTO
//* Oculta los atributos de la clase
//* Hacerlos locales dentro de la clase.
//* El simbolo " _ "

//CLASES
class user {
  //propiedades
  String? nombre;
  int? edad;

  //METODOS
  void report() {
    print(edad);
    print(nombre);
  }
}

class estudiante {
  String? carrera;
  String? Ncuenta;
  int? Semestre;

  void reporrt() {
    print("Carrera : $carrera ");
    print("No Cuenta : $Ncuenta ");
    print("Semestre : $Semestre ");
  }
// }
// -------------------------------------------------------------------
void main(List<String> args) {
  user usuario = user();
  usuario.nombre = "marco";
  usuario.edad = 21;
  usuario.reporte();
}

class user {
  String? _nombre;
  int? _edad;

  // El seter solo se puede utilizar con un valor
  // sirve sin el void tambien
  void set nombre(String nombre) {
    //mandas llamar la variable y le asignas el valor para tenerla "privada"
    _nombre = nombre;
  }

  set edad(int edad) {
    _edad = edad;
  }

  String get nombre {
    return _nombre!;
  }

  void reporte() {
    print(_nombre);
    print(_edad);
  }
}

// int x = 25;
// void main(List<String> args) {
//   var y = 5;
//   void Shownum() {
//     var x = 10;
//     print(x);
//     print(y);
//   }

//   //funciones fat arrow
//   void showx2() => print(x); //funciones declarativas

//   Shownum();
// }
