package X_final;

import java.util.Stack;

public class ArbolDeExpresion {
    private Nodo raiz;

    public ArbolDeExpresion(String postfijo) {
        Stack<Nodo> pila = new Stack<>();
        for (String token : postfijo.split("\\s+")) {
            if (esOperador(token)) {
                Nodo nodo = new Nodo(token);
                if (token.equals("!")) {
                    if (pila.isEmpty()) {
                        throw new IllegalArgumentException("Expresión inválida: no hay suficientes operandos para '!'");
                    }
                    nodo.derecha = pila.pop();
                } else {
                    if (pila.isEmpty()) {
                        throw new IllegalArgumentException(
                                "Expresión inválida: no hay suficientes operandos para '" + token + "'");
                    }
                    nodo.derecha = pila.pop();
                    if (pila.isEmpty()) {
                        throw new IllegalArgumentException(
                                "Expresión inválida: no hay suficientes operandos para '" + token + "'");
                    }
                    nodo.izquierda = pila.pop();
                }
                pila.push(nodo);
            } else {
                pila.push(new Nodo(token));
            }
        }

        if (pila.size() != 1) {
            return;
        }

        raiz = pila.pop();
    }

    public double evaluar() {
        return evaluar(raiz);
    }

    private double evaluar(Nodo nodo) {
        if (nodo == null) {
            return 0;
        }
        if (!esOperador(nodo.valor)) {
            return Double.parseDouble(nodo.valor);
        }
        double izquierda = evaluar(nodo.izquierda);
        double derecha = evaluar(nodo.derecha);
        switch (nodo.valor) {
            case "+":
                return izquierda + derecha;
            case "-":
                return izquierda - derecha;
            case "*":
                return izquierda * derecha;
            case "/":
                return izquierda / derecha;
            case "!":
                return factorial(derecha);
            default:
                return 0;
        }
    }

    private boolean esOperador(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/") || token.equals("!");
    }

    private double factorial(double num) {
        if (num == 0) {
            return 1;
        }
        double resultado = 1;
        for (int i = 1; i <= num; i++) {
            resultado *= i;
        }
        return resultado;
    }
}
