fun main(args: Array<String>) {

    val a = 20
    val b = 10

    // SUMA
    val suma1 = a + b
    val suma2 = a.plus(b)
    println("Suma:  $suma1 / $suma2")

    // RESTA
    val resta1 = a - b
    val resta2 = a.minus(b)
    println("Resta: $resta1 / $resta2")

    // MULTIPLICACION
    val mult1 = a * b
    val mult2 = a.times(b)
    println("Multiplicacion: $mult1 / $mult2")

    // DIVISION
    val div1 = a / b
    val div2 = a.div(b)
    println("Division: $div1 / $div2")

    // MODULO
    val mod1 = a % b
    val mod2 = a.rem(b)
    println("Modulo (resto): $mod1 / $mod2")

    // INCREMENTO
    var c = a
    c++
    val incFun = a.inc()
    println("Incremento: $c / $incFun")

    // DECREMENTO
    var d = a
    d--
    val decFun = a.dec()
    println("Decremento: $d / $decFun")

    // MAYOR QUE
    val mayor1 = a > b
    val mayor2 = a.compareTo(b) > 0
    println("Mayor que: $mayor1 / $mayor2")

    // MENOR QUE
    val menor1 = a < b
    val menor2 = a.compareTo(b) < 0
    println("Menor que: $menor1 / $menor2")

    // MAYOR O IGUAL
    val mayorIgual1 = a >= b
    val mayorIgual2 = a.compareTo(b) >= 0
    println("Mayor o igual: $mayorIgual1 / $mayorIgual2")

    // MENOR O IGUAL
    val menorIgual1 = a <= b
    val menorIgual2 = a.compareTo(b) <= 0
    println("Menor o igual: $menorIgual1 / $menorIgual2")

    // DISTINTO
    val distinto1 = a != b
    val distinto2 = !a.equals(b)
    println("Distinto: $distinto1 / $distinto2")
}
