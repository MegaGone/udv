package X_final;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> infixExpressions = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("expresiones.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                infixExpressions.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        for (String infix : infixExpressions) {
            try {
                String postfix = InfixToPostfix.convert(infix);
                ExpressionTree tree = new ExpressionTree(postfix);
                double result = tree.evaluate();
                System.out.println("Infix: " + infix);
                System.out.println("Postfix: " + postfix);
                System.out.println("Result: " + result);
            } catch (Exception e) {
                System.out.println("Error processing expression: " + infix);
                e.printStackTrace();
            }
        }
    }
}
