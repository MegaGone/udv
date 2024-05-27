package X_final;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> infixExpressions = LectorArchivo.leerExpresiones("expresiones.txt");

        for (String infix : infixExpressions) {
            try {
                String postfix = InfixToPostfix.convert(infix);
                ExpressionTree tree = new ExpressionTree(postfix);
                double result = tree.evaluate();
                System.out.println("INFIJA: " + infix);
                System.out.println("POSTFIJA: " + postfix);
                System.out.println("RESULTADO: " + result + "\n");
            } catch (Exception e) {
                System.out.println("[ERROR] HA OCURRIDO UN ERROR AL PROCESAR LA EXPRESIÓN: " + infix);
                e.printStackTrace();
            }
        }
    }
}
