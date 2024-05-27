package X_final;

import java.util.Stack;

public class InfixToPostfix {
    public static String convert(String infix) {
        StringBuilder postfix = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        boolean previousWasOperator = true; // Para manejar números negativos

        for (char ch : infix.toCharArray()) {
            if (Character.isDigit(ch) || ch == '.') {
                postfix.append(ch);
                previousWasOperator = false;
            } else if (ch == '(') {
                stack.push(ch);
                previousWasOperator = true;
            } else if (ch == ')') {
                while (!stack.isEmpty() && stack.peek() != '(') {
                    postfix.append(' ').append(stack.pop());
                }
                stack.pop();
                previousWasOperator = false;
            } else if (isOperator(ch)) {
                if (previousWasOperator && ch == '-') {
                    postfix.append(ch); // Manejar el signo negativo
                } else {
                    postfix.append(' ');
                    while (!stack.isEmpty() && precedence(ch) <= precedence(stack.peek())) {
                        postfix.append(stack.pop()).append(' ');
                    }
                    stack.push(ch);
                    previousWasOperator = true;
                }
            }
        }

        while (!stack.isEmpty()) {
            postfix.append(' ').append(stack.pop());
        }

        return postfix.toString().trim();
    }

    private static boolean isOperator(char ch) {
        return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '!';
    }

    private static int precedence(char ch) {
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
