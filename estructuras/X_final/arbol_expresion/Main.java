package arbol_expresion;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/X_final/arbol_expresion/

import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> expresionesInfijas = LectorArchivo.leerExpresiones("expresiones.txt");

        for (String infija : expresionesInfijas) {
            try {
                String postfija = Conversor.convertir(infija);
                ArbolDeExpresion arbol = new ArbolDeExpresion(postfija);
                double resultado = arbol.evaluar();
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
