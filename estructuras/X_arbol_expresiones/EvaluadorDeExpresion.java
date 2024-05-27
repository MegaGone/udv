package X_arbol_expresiones;

public class EvaluadorDeExpresion {
    public double evaluar(NodoArbol nodo) {
        if (nodo == null) {
            return 0;
        }

        if (nodo.izquierda == null && nodo.derecha == null) {
            return Double.parseDouble(nodo.valor);
        }

        double izquierdo = evaluar(nodo.izquierda);
        double derecho = evaluar(nodo.derecha);

        switch (nodo.valor) {
            case "+":
                return izquierdo + derecho;
            case "-":
                return izquierdo - derecho;
            case "*":
                return izquierdo * derecho;
            case "/":
                return izquierdo / derecho;
            case "^":
                return Math.pow(izquierdo, derecho);
            case "!":
                return factorial(derecho);
        }
        throw new IllegalArgumentException("Operador desconocido: " + nodo.valor);
    }

    private double factorial(double numero) {
        int n = (int) numero;
        int resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
}
