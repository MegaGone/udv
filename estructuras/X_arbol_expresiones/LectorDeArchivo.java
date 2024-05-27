package X_arbol_expresiones;

import java.io.*;
import java.util.List;
import java.util.ArrayList;

public class LectorDeArchivo {
    public List<String> leerLineas(String archivo) throws IOException {
        List<String> lineas = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(archivo))) {
            String line;
            while ((line = br.readLine()) != null) {
                lineas.add(line);
            }
        }
        return lineas;
    }
}