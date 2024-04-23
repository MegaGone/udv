import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/IX_pila/
// NOTA: Ejecutar con el comando java Parentesis

public class Parentesis {

    private static boolean esParentesisDeApertura(char ch) {
        return ch == '(' || ch == '[' || ch == '{';
    }

    private static boolean esParentesisDeCierre(char ch) {
        return ch == ')' || ch == ']' || ch == '}';
    }

    private static char validarParentesis(char openingBracket) {
        switch (openingBracket) {
            case '(':
                return ')';
            case '[':
                return ']';
            case '{':
                return '}';
            default:
                throw new IllegalArgumentException("Invalid opening bracket: " + openingBracket);
        }
    }

    public static boolean validarBalance(String expression) {
        Pila<Character> pila = new Pila<>();

        for (int i = 0; i < expression.length(); i++) {
            char ch = expression.charAt(i);

            if (esParentesisDeApertura(ch)) {
                pila.stack(ch);
            } else if (esParentesisDeCierre(ch)) {
                if (pila.isEmpty()) {
                    return false; // PARÉNTESIS SIN APERTURA
                }

                char top = pila.unStack();
                if (validarParentesis(top) != ch) {
                    return false; // CIERRE NO COINCIDE CON SIGNO DE APERTURA
                }
            }
        }

        return pila.isEmpty(); // SI ESTÁ VACÍA ES PORQUE ESTEÁ BALANCEADA, DE LO CONTRARIO NO ESTÁ BALANCEADA
    }

    public static String pedirExpresion() {
        Scanner scanner = null;
        try {
            scanner = new Scanner(System.in);
            System.out.print("Ingrese la expresión: ");
            return scanner.nextLine();
        } finally {
            if (scanner != null) {
                scanner.close();
            }
        }
    }

    public static void main(String[] args) {
        String expression = pedirExpresion();
        boolean balanced = validarBalance(expression);
        System.out.println("***** EXPRESION A EVALUAR *****");
        System.out.println(expression);

        if (balanced) {
            System.out.println("\nEXPRESION BALANCEADA.");
        } else {
            System.out.println("\nEXPRESION NO BALANCEADA.");
        }
    }
}
