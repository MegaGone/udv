package X_arbol_expresiones;

import java.util.Stack;

public class ArbolDeExpresion {
    public NodoArbol construirArbol(String postfija) {
        Stack<NodoArbol> stack = new Stack<>();
        String[] tokens = postfija.split(" ");

        for (String token : tokens) {
            if (!esOperador(token)) {
                stack.push(new NodoArbol(token));
            } else {
                NodoArbol node = new NodoArbol(token);
                if (token.equals("!")) {
                    if (stack.isEmpty()) throw new IllegalArgumentException("Expresión posfija inválida: falta operando para el operador '!'");
                    node.derecha = stack.pop();
                } else if (token.equals("-") && (stack.isEmpty() || !esOperador(stack.peek().valor))) {
                    if (stack.isEmpty()) throw new IllegalArgumentException("Expresión posfija inválida: falta operando para el operador unario '-'.");
                    node.derecha = stack.pop();
                } else {
                    if (stack.isEmpty()) throw new IllegalArgumentException("Expresión posfija inválida: falta operando para el operador '" + token + "'");
                    node.derecha = stack.pop();
                    if (stack.isEmpty()) throw new IllegalArgumentException("Expresión posfija inválida: falta operando para el operador '" + token + "'");
                    node.izquierda = stack.pop();
                }
                stack.push(node);
            }
        }
        return stack.pop();
    }

    private boolean esOperador(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/") || token.equals("!") || token.equals("^");
    }
}
