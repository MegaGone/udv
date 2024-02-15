import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/I_posteriori.java

public class I_Posteriori {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresar valores separados por espacios, comas o puntos: ");
        String input = scanner.nextLine();

        int[] values = handleValues(input.split("[,\\s.]+"));

        long startTime = System.nanoTime();
        int max = findMaxValue(values);
        long endTime = System.nanoTime();

        startAnalytics(startTime, endTime, max);

        scanner.close();
    }

    private static int[] handleValues(String[] rawValues) {
        int[] values = new int[rawValues.length];
        for (int i = 0; i < rawValues.length; i++) {
            values[i] = Integer.parseInt(rawValues[i].trim());
        }
        return values;
    }

    private static int findMaxValue(int[] array) {
        int max = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > max) {
                max = array[i];
            }
        }
        return max;
    }

    private static void startAnalytics(long startTime, long endTime, int max) {
        long elapsedTime = (endTime - startTime);

        Runtime runtime = Runtime.getRuntime();
        long usedMemory = runtime.totalMemory() - runtime.freeMemory();

        long cpuUsage = elapsedTime * (1000000 / elapsedTime);

        System.out.println("El valor más grande en el array es: " + max);
        System.out.println("Uso de CPU: " + cpuUsage + " nanosegundos");
        System.out.println("Memoria utilizada: " + usedMemory + " bytes");
        System.out.println("Tiempo transcurrido: " + elapsedTime + " nanosegundos");
    }
}
