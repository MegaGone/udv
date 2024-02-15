import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/II_posteriori.java

public class II_posteriori {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresar valores separados por espacios, comas o puntos: ");
        String input = scanner.nextLine();

        int[] values = processValues(input.split("[,\\s.]+"));

        long startTime = System.nanoTime();
        int max = findMaxDifference(values);
        long endTime = System.nanoTime();

        startAnalytics(startTime, endTime, max);

        scanner.close();
    }

    private static int[] processValues(String[] rawValues) {
        int[] values = new int[rawValues.length];
        for (int i = 0; i < rawValues.length; i++) {
            values[i] = Integer.parseInt(rawValues[i].trim());
        }
        return values;
    }

    private static int findMaxDifference(int[] array) {
        int n = array.length;
        int maxDifference = 0;

        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int difference = Math.abs(array[i] - array[j]);
                if (difference > maxDifference) {
                    maxDifference = difference;
                }
            }
        }

        return maxDifference;
    }

    private static void startAnalytics(long startTime, long endTime, int max) {
        long elapsedTime = (endTime - startTime);

        Runtime runtime = Runtime.getRuntime();
        long usedMemory = runtime.totalMemory() - runtime.freeMemory();

        long cpuUsage = elapsedTime * (1000000 / elapsedTime);

        System.out.println("La mayor diferencia en el array es: " + max);
        System.out.println("Uso de CPU: " + cpuUsage + " nanosegundos");
        System.out.println("Memoria utilizada: " + usedMemory + " bytes");
        System.out.println("Tiempo transcurrido: " + elapsedTime + " nanosegundos");
    }
}
