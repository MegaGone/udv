package X_arbol_expresiones;

import java.util.Stack;
import java.util.List;
import java.util.ArrayList;

public class ConversorDeExpresiones {
    public String convertir(String infija) {
        Stack<Character> stack = new Stack<>();
        List<String> salida = new ArrayList<>();
        StringBuilder numero = new StringBuilder();
        boolean anteriorEsOperador = true;
        char[] tokens = infija.toCharArray();

        for (char token : tokens) {
            if (Character.isDigit(token) || token == '.') {
                numero.append(token);
                anteriorEsOperador = false;
            } else {
                if (numero.length() > 0) {
                    salida.add(numero.toString());
                    numero.setLength(0);
                }
                if (token == '(') {
                    stack.push(token);
                    anteriorEsOperador = true;
                } else if (token == ')') {
                    while (!stack.isEmpty() && stack.peek() != '(') {
                        salida.add(String.valueOf(stack.pop()));
                    }
                    stack.pop();
                    anteriorEsOperador = false;
                } else if (esOperador(token)) {
                    if (anteriorEsOperador && token == '-') {
                        numero.append(token);
                        anteriorEsOperador = false;
                    } else {
                        while (!stack.isEmpty() && precedencia(stack.peek()) >= precedencia(token)) {
                            salida.add(String.valueOf(stack.pop()));
                        }
                        stack.push(token);
                        anteriorEsOperador = true;
                    }
                }
            }
        }

        if (numero.length() > 0) {
            salida.add(numero.toString());
        }

        while (!stack.isEmpty()) {
            salida.add(String.valueOf(stack.pop()));
        }

        return String.join(" ", salida);
    }

    private boolean esOperador(char token) {
        return token == '+' || token == '-' || token == '*' || token == '/' || token == '!' || token == '^';
    }

    private int precedencia(char operador) {
        switch (operador) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            case '^':
                return 3;
            case '!':
                return 4;
            default:
                return -1;
        }
    }
}
