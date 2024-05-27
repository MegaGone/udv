package arbol_expresion;

import java.io.*;
import java.util.*;

public class LectorArchivo {
    public static List<String> leerExpresiones(String nombreArchivo) {
        List<String> expresionesInfijas = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(nombreArchivo))) {
            String linea;
            while ((linea = br.readLine()) != null) {
                expresionesInfijas.add(linea);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return expresionesInfijas;
    }
}
