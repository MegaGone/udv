package X_arbol_expresiones;

import java.io.IOException;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        LectorDeArchivo archivoDeEntrada = new LectorDeArchivo();
        ArbolDeExpresion arbolDeExpresion = new ArbolDeExpresion();
        EvaluadorDeExpresion evaluador = new EvaluadorDeExpresion();
        ConversorDeExpresiones conversor = new ConversorDeExpresiones();

        try {
            List<String> expresiones = archivoDeEntrada.leerLineas("expresiones.txt");
            for (String expresion : expresiones) {
                String postfija = conversor.convertir(expresion);
                System.out.println("Expresión posfija: " + postfija);

                NodoArbol raiz = arbolDeExpresion.construirArbol(postfija);
                double resultado = evaluador.evaluar(raiz);
                System.out.println("Resultado: " + resultado);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
