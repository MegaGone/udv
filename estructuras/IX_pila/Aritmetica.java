import java.util.Stack;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/IX_pila/
// NOTA: Ejecutar con el comando java Aritmetica

public class Aritmetica {

    private static final String OPERADORES = "+-*/";

    public String infijoAPostfijo(String expresion) {
        StringBuilder posfijo = new StringBuilder();
        Stack<Character> pila = new Stack<>();

        for (char c : expresion.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                agregarAlPosfijo(posfijo, c);
            } else if (esOperador(c)) {
                procesarOperador(pila, posfijo, c);
            } else if (c == '(') {
                pila.push('(');
            } else if (c == ')') {
                procesarParentesis(pila, posfijo);
            }
        }

        vaciarPilaEnPosfijo(pila, posfijo);

        return posfijo.toString();
    }

    private void agregarAlPosfijo(StringBuilder posfijo, char c) {
        posfijo.append(c);
    }

    private void procesarOperador(Stack<Character> pila, StringBuilder posfijo, char c) {
        while (!pila.isEmpty() && precedencia(pila.peek()) >= precedencia(c)) {
            posfijo.append(pila.pop());
        }
        pila.push(c);
    }

    private void procesarParentesis(Stack<Character> pila, StringBuilder posfijo) {
        while (!pila.isEmpty() && pila.peek() != '(') {
            posfijo.append(pila.pop());
        }
        pila.pop();
    }

    private void vaciarPilaEnPosfijo(Stack<Character> pila, StringBuilder posfijo) {
        while (!pila.isEmpty()) {
            posfijo.append(pila.pop());
        }
    }

    private int precedencia(char operador) {
        switch (operador) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
                return 2;
            default:
                return 0;
        }
    }

    private boolean esOperador(char c) {
        return OPERADORES.contains(Character.toString(c));
    }

    public static void main(String[] args) {
        Aritmetica aritmetica = new Aritmetica();
        String expresionInfija = "(a + b)";
        String expresionPosfija = aritmetica.infijoAPostfijo(expresionInfija);

        System.out.println("\nEXPRESION INFIJA: " + expresionInfija);
        System.out.println("\nEXPRESION POSTFIJA: " + expresionPosfija);
    }
}
