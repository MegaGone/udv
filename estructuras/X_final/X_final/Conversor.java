package X_final;

import java.util.Stack;

public class Conversor {
    public static String convertir(String infijo) {
        StringBuilder postfijo = new StringBuilder();
        Stack<Character> pila = new Stack<>();
        boolean anteriorFueOperador = true; // MANEJAR NÚMEROS NEGATIVOS

        for (char ch : infijo.toCharArray()) {
            if (Character.isDigit(ch) || ch == '.') {
                postfijo.append(ch);
                anteriorFueOperador = false;
            } else if (ch == '(') {
                pila.push(ch);
                anteriorFueOperador = true;
            } else if (ch == ')') {
                while (!pila.isEmpty() && pila.peek() != '(') {
                    postfijo.append(' ').append(pila.pop());
                }
                pila.pop();
                anteriorFueOperador = false;
            } else if (esOperador(ch)) {
                if (anteriorFueOperador && ch == '-') {
                    postfijo.append(ch); // MANEJAR SIGNO NEGATIVO -
                } else {
                    postfijo.append(' ');
                    while (!pila.isEmpty() && precedencia(ch) <= precedencia(pila.peek())) {
                        postfijo.append(pila.pop()).append(' ');
                    }
                    pila.push(ch);
                    anteriorFueOperador = true;
                }
            }
        }

        while (!pila.isEmpty()) {
            postfijo.append(' ').append(pila.pop());
        }

        return postfijo.toString().trim();
    }

    private static boolean esOperador(char ch) {
        return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '!';
    }

    private static int precedencia(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '!':
                return 3;
            default:
                return -1;
        }
    }
}
