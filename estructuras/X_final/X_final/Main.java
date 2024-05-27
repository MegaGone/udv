package X_final;

import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> expresionesInfijas = LectorArchivo.leerExpresiones("expresiones.txt");

        for (String infija : expresionesInfijas) {
            try {
                String postfija = InfixToPostfix.convert(infija);
                ExpressionTree arbol = new ExpressionTree(postfija);
                double resultado = arbol.evaluate();
                System.out.println("INFIJA: " + infija);
                System.out.println("POSTFIJA: " + postfija);
                System.out.println("RESULTADO: " + resultado + "\n");
            } catch (Exception e) {
                System.out.println("[ERROR][EXPRESION]: " + infija);
                e.printStackTrace();
            }
        }
    }
}
