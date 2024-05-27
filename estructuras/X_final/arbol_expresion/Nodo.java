package arbol_expresion;

public class Nodo {
    String valor;
    Nodo derecha;
    Nodo izquierda;

    Nodo(String valor) {
        this.valor = valor;
        this.derecha = null;
        this.izquierda = null;
    }
}
