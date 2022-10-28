main() {
  // var carro = vehiculo();

  // carro.Nllantas = 4;
  // carro.color = "Negro";
  // carro.marca = "Mercedez";
  // carro.modelo = "AMG G63";
  // carro.espec();
  // carro.arrancar();
  // carro.correr();
  // carro.frenar();
}

class vehiculo {
  int? _Nllantas;
  String? _color;
  String? _modelo;
  String? _Marca;

  set Nllantas(int Nllantas) => _Nllantas = Nllantas;
  set color(String color) => _color = color;
  set modelo(String modelo) => _modelo = modelo;
  set marca(String marca) => _Marca = marca;

  int get Nllantas => _Nllantas!;
  String get color => _color!;
  String get modelo => _modelo!;
  String get marca => _Marca!;

  void arrancar() => print("Ya esta prendiendo pa,aguanta");
  void correr() => print("Vas en burgisa pa, dale leve");
  void frenar() => print("*sonido de balatas viejas*");

  void espec() {
    print("Especificaciones del vehiculo: \n");
    print("Tienes un :$_Marca");
    print("Ah perro tienes un :$_modelo ");
    print("El color del vehiculo es: $_color");
    print("Tienes : $_Nllantas llantas pa");
  }

  vehiculo(this._Nllantas, this._color, this._Marca, this._modelo);
}

//Constructores
// vehiculo.apellido asi podemos tener varios constructores en la misma clases
//tiene que tener el mismo nombre de la clase
