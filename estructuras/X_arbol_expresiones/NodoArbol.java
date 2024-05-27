package X_arbol_expresiones;

public class NodoArbol {
    String valor;
    NodoArbol derecha;
    NodoArbol izquierda;

    NodoArbol(String _valor) {
        this.valor = _valor;
        this.derecha = null;
        this.izquierda = null;
    }
}
