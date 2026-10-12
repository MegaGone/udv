// 1. MutableList

//fun main() {
//    val languages = mutableListOf("Kotlin", "Java")
//    languages.add("Swift")
//    languages.add(1, "Dart")
//    languages.addAll(listOf("Go", "Rust"))
//    languages[0] = "Kotlin 2.0"
//    languages.remove("Java")
//    languages.removeAt(0)
//    println(languages)
//}

// 2. MutableSet
//fun main() {
//    val ids = mutableSetOf(1, 2, 3)
//    ids.add(4)
//    ids.add(2)
//    ids.addAll(setOf(5, 6))
//    ids.retainAll(setOf(2, 4, 6, 8))
//    ids.remove(2)
//    println(ids)
//}

// 3. MutableMap

fun main() {
    val stock = mutableMapOf("manzana" to 10, "pera" to 5)
    stock["banano"] = 8
    stock["manzana"] = 12
    stock.putAll(mapOf("uva" to 20))
    stock.getOrPut("kiwi") { 3 }
    stock.remove("pera")
    println(stock)
}

// 4. Conversión entre colecciones inmutables y mutables

//fun main() {
//    val readOnly = listOf("a", "b", "c")
//    val editable = readOnly.toMutableList()
//    editable.add("d")
//    val backToReadOnly = editable.toList()
//    println(backToReadOnly)
//}
