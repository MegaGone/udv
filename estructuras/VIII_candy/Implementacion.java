import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/VIII_candy/
// NOTA: Ejecutar con el comando java Implementacion

public class Implementacion {

    public static void main(String[] args) {
        Implementacion candy = new Implementacion();
        candy.start();
    }

    private void start() {
        String[] paquete = solicitarDulces();
        simularProceso(paquete);
    }

    private String[] solicitarDulces() {
        Scanner scanner = new Scanner(System.in);
        String[] list = new String[5];

        for (int i = 0; i < 5; i++) {
            System.out.print("Ingrese el color del caramelo " + (i + 1) + ": ");
            String input = scanner.nextLine();

            if (!esString(input)) {
                System.out.println("Error: Debe ingresar un caramelo de color de tipo String.");
                i--;
                continue;
            }

            list[i] = input.toLowerCase();
        }

        scanner.close();
        return list;
    }

    private boolean esString(String input) {
        return input != null && !input.isEmpty();
    }

    private void simularProceso(String[] paquete) {
        Pila<String> pilaTemporal = new Pila<>();
        System.out.println("\n************* COMIENDO DULCES *************\n");

        for (int i = paquete.length - 1; i >= 0; i--) {
            String caramelo = paquete[i];
            if (!caramelo.equals("amarillo")) {
                pilaTemporal.stack(caramelo);
                System.out.println("Agregando a la pila el caramelo color " + caramelo);
            } else {
                System.out.println("!!! Caramelo amarillo encontrado !!!");
            }
        }

        System.out.println("\nEl paquete final, sin caramelos amarillos, es:");
        while (!pilaTemporal.isEmpty()) {
            String caramelo = pilaTemporal.unStack();
            System.out.println(caramelo);
        }
    }

}