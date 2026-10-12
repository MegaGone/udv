// 1. Sintaxis básica

//class User {
//    var name: String = ""
//    var age: Int = 0
//    var email: String = ""
//}
//
//fun main() {
//    val user = User().apply {
//        name = "Jimmy"
//        age = 24
//        email = "jimmy@gmail.com"
//    }
//    println("${user.name}, ${user.age}, ${user.email}")
//}

// 2. apply devuelve el propio objeto

//fun main() {
//    val numbers = mutableListOf<Int>().apply {
//        add(10)
//        add(20)
//        add(30)
//    }
//    // apply devolvio la lista, por eso se puede seguir usando
//    println(numbers)
//    println(numbers.sum())
//}

// 3. apply frente a las demás funciones de alcance

//fun main() {
//    val builder = StringBuilder()
//    val text = builder.apply {
//        append("Hola")
//        append(", ")
//        append("Kotlin")
//    }.toString()           // apply devuelve el StringBuilder; luego toString()
//    println(text)
//}

// 4. Ejemplo desarrollo móvil

class TextView {
    var text: String = ""
    var textSize: Int = 12
    var visible: Boolean = true
    fun render() = "[$text | size=$textSize | visible=$visible]"
}

fun main() {
    val title = TextView().apply {
        text = "Bienvenido"
        textSize = 20
        visible = true
    }
    println(title.render())
}
