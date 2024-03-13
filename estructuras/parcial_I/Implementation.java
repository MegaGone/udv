import TDA.Fraccion;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/parcial_I/TDA/Implementation.java

public class Implementation {
    public static void main(String[] args) {
        // Crear instancias de Fraccion para realizar pruebas
        Fraccion fraccion1 = new Fraccion(1, 2);
        Fraccion fraccion2 = new Fraccion(3, 4);

        // Pruebas de los métodos getter
        System.out.println("Numerador de fraccion1: " + fraccion1.getNumerador());
        System.out.println("Denominador de fraccion1: " + fraccion1.getDenominador());
        System.out.println("Numerador de fraccion2: " + fraccion2.getNumerador());
        System.out.println("Denominador de fraccion2: " + fraccion2.getDenominador());

        // Pruebas de los métodos setter
        fraccion1.setNumerador(2);
        fraccion1.setDenominador(3);
        System.out.println("Fraccion1 modificada: " + fraccion1);
        System.out.println("Fraccion2 modificada: " + fraccion2);

        // Pruebas de operaciones aritméticas
        System.out.println("\n" + "----- PRUEBAS ARITMETICAS -----");
        testOperacionesAritmeticas(fraccion1, fraccion2);

        // Pruebas de otros métodos
        System.out.println("\n" + "----- OTRAS ARITMETICAS -----");
        testOtrosMetodos(fraccion1);

        // Mostrar la fraccion
        fraccion1.mostrarFraccion();
        fraccion1.mostrarNumerador();
        fraccion1.mostrarDenominador();
    }

    public static void testOperacionesAritmeticas(Fraccion fraccion1, Fraccion fraccion2) {
        Fraccion resultadoSuma = fraccion1.suma(fraccion2);
        System.out.println("Suma de fraccion1 y fraccion2: " + resultadoSuma);

        Fraccion resultadoResta = fraccion1.resta(fraccion2);
        System.out.println("Resta de fraccion1 y fraccion2: " + resultadoResta);

        Fraccion resultadoMultiplicacion = fraccion1.multiplicacion(fraccion2);
        System.out.println("Multiplicación de fraccion1 y fraccion2: " + resultadoMultiplicacion);

        Fraccion resultadoDivision = fraccion1.division(fraccion2);
        System.out.println("División de fraccion1 y fraccion2: " + resultadoDivision);
    }

    public static void testOtrosMetodos(Fraccion fraccion1) {
        System.out.println("Fraccion1 simplificada: " + fraccion1.simplificacion());
        System.out.println("¿Fraccion1 es nula? " + fraccion1.esNula());
        System.out.println("¿Fraccion1 es una fraccion propia? " + fraccion1.esFraccionPropia());
    }
}
