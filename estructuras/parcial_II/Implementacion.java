package parcial_II;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/parcial_II/Implementacion.java

import java.util.Scanner;

public class Implementacion {

    public static void main(String[] args) {
        ColaMedieval cola = new ColaMedieval();

        solicitarPersonajes(cola);

        System.out.println("***************************************************\n");
        System.out.println("EL PRIMERO EN LA COLA ES: " + cola.consultarPrimero());
        System.out.println("ELIMINANDO PRIMERO EN LA COLA " + "(" + cola.consultarPrimero() + ")");
        cola.quitarPrimero();
        System.out.println("EL PRIMERO EN LA COLA ACTUALIZADA ES: " + cola.consultarPrimero());
        System.out.println("NUMERO DE NOBLES EN LA COLA " + cola.consultarNumeroNobles());
        System.out.println("NUMERO DE PLEBEYOS EN LA COLA: " + cola.consultarNumeroPlebeyos());
        System.out.println("¿ESTA VACIA LA COLA? " + cola.esVacia());
        System.out.println("\n***************************************************");
    }

    private static void solicitarPersonajes(ColaMedieval cola) {
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            System.out.println("Ingrese el nombre del personaje " + i + 1 + ":");
            String nombre = scanner.nextLine();
            while (!esNombreValido(nombre)) {
                System.out.println(
                        "El nombre del personaje debe ser una cadena de caracteres. Por favor, ingrese un nombre válido:");
                nombre = scanner.nextLine();
            }

            System.out.println("¿Es noble? (Si/No):");
            String respuesta = scanner.nextLine().toLowerCase();
            while (!esRespuestaValida(respuesta)) {
                System.out.println("Por favor, responda 'Si' o 'No':");
                respuesta = scanner.nextLine().toLowerCase();
            }
            boolean esNoble = respuesta.equals("si");

            cola.añadir(nombre, esNoble);
        }

        scanner.close();
    }

    private static boolean esNombreValido(String nombre) {
        return !nombre.isEmpty();
    }

    private static boolean esRespuestaValida(String respuesta) {
        return respuesta.equals("si") || respuesta.equals("no");
    }
}
