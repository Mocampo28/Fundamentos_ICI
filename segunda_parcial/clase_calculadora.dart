//calculadora que sume, reste, multiplique y divida 2 numeros como arguemntos

void main() {
  var oper = calcu();
  oper.a = 5; // convertimos en propiedades de la clase
  oper.b = 5;

  //se ponen "{}" parapoder utilizar las propiedades como variables para que funcione
  print("${oper.a} + ${oper.b} = ${oper.suma(oper.a, oper.b)}");
  //utilizamos las propiedades en las variables
  print("${oper.a} - ${oper.b} = ${oper.rest(oper.a, oper.b)}");
  print("${oper.a} * ${oper.b} = ${oper.multi(oper.a, oper.b)}");
  print(
      "${oper.a} / ${oper.b} = ${oper.div(oper.a.toDouble(), oper.b.toDouble())}");
  //convierto los int a double para la div.
}

class calcu {
  int a = 0;
  int b = 0;

  int suma(int a, int b) => a + b; //Metodos de la clase calculadora
  int rest(int a, int b) => a - b; //Operaciones basicas
  int multi(int a, int b) => a * b;
  double div(double a, double b) => a / b;
}

void main(List<String> args) {
  print("121212");
  int n1 = 0;
  int n2 = 0;
  if (args.length < 1) {
    n1 = int.parse(args[0]);
    n2 = int.parse(args[1]);
  } else {
    print("Asi no wey");
  }
}
