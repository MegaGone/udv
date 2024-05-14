package parcial_II;

import java.util.LinkedList;

public class ColaMedieval implements IColaMedieval {
    private LinkedList<String> nobles;
    private LinkedList<String> plebeyos;
    private int tamañoNobles;
    private int tamañoPlebeyos;

    public ColaMedieval() {
        nobles = new LinkedList<>();
        plebeyos = new LinkedList<>();
        tamañoNobles = 0;
        tamañoPlebeyos = 0;
    }

    public void añadir(String elemento, boolean esNoble) {
        (esNoble ? nobles : plebeyos).add(elemento);
        if (esNoble) {
            tamañoNobles++;
        } else {
            tamañoPlebeyos++;
        }
    }

    public String consultarPrimero() {
        return (!nobles.isEmpty()) ? nobles.getFirst() : (!plebeyos.isEmpty()) ? plebeyos.getFirst() : null;
    }

    public void quitarPrimero() {
        if (!nobles.isEmpty()) {
            nobles.removeFirst();
            tamañoNobles--;
        } else if (!plebeyos.isEmpty()) {
            plebeyos.removeFirst();
            tamañoPlebeyos--;
        }
    }

    public int consultarNumeroNobles() {
        return tamañoNobles;
    }

    public int consultarNumeroPlebeyos() {
        return tamañoPlebeyos;
    }

    public boolean esVacia() {
        return nobles.isEmpty() && plebeyos.isEmpty();
    }
}
