package X_final;

import java.util.Stack;

public class ExpressionTree {
    private Node root;

    public ExpressionTree(String postfix) {
        Stack<Node> stack = new Stack<>();
        for (String token : postfix.split("\\s+")) {
            if (isOperator(token)) {
                Node node = new Node(token);
                if (token.equals("!")) {
                    if (stack.isEmpty()) {
                        throw new IllegalArgumentException("Invalid expression: not enough operands for '!'");
                    }
                    node.right = stack.pop();
                } else {
                    if (stack.isEmpty()) {
                        throw new IllegalArgumentException("Invalid expression: not enough operands for '" + token + "'");
                    }
                    node.right = stack.pop();
                    if (stack.isEmpty()) {
                        throw new IllegalArgumentException("Invalid expression: not enough operands for '" + token + "'");
                    }
                    node.left = stack.pop();
                }
                stack.push(node);
            } else {
                stack.push(new Node(token));
            }
        }

        if (stack.size() != 1) {
            return;
        }

        root = stack.pop();
    }

    public double evaluate() {
        return evaluate(root);
    }

    private double evaluate(Node node) {
        if (node == null) {
            return 0;
        }
        if (!isOperator(node.value)) {
            return Double.parseDouble(node.value);
        }
        double left = evaluate(node.left);
        double right = evaluate(node.right);
        switch (node.value) {
            case "+":
                return left + right;
            case "-":
                return left - right;
            case "*":
                return left * right;
            case "/":
                return left / right;
            case "!":
                return factorial(right);
            default:
                return 0;
        }
    }

    private boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("*") || token.equals("/") || token.equals("!");
    }

    private double factorial(double num) {
        if (num == 0) {
            return 1;
        }
        double result = 1;
        for (int i = 1; i <= num; i++) {
            result *= i;
        }
        return result;
    }

    private static class Node {
        String value;
        Node left, right;

        Node(String value) {
            this.value = value;
        }
    }
}
