import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/IV_bubble_sort.java

public class IV_BubbleSort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresar valores separados por espacios, comas o puntos: ");
        String input = scanner.nextLine();

        int[] values = handleValues(input.split("[,\\s.]+"));

        long startTime = System.nanoTime();
        bubbleSort(values);
        long endTime = System.nanoTime();

        startAnalytics(startTime, endTime);

        scanner.close();
    }

    private static int[] handleValues(String[] rawValues) {
        int[] values = new int[rawValues.length];
        for (int i = 0; i < rawValues.length; i++) {
            values[i] = Integer.parseInt(rawValues[i].trim());
        }
        return values;
    }

    private static void bubbleSort(int[] array) {
        int indexOfLastUnsortedElement = array.length;
        boolean swapped;
        int swapCounter = 0;
        do {
            swapped = false;
            for (int i = 0; i < indexOfLastUnsortedElement - 1; i++) {
                if (array[i] > array[i + 1]) {
                    int temp = array[i];
                    array[i] = array[i + 1];
                    array[i + 1] = temp;
                    swapped = true;
                    swapCounter++;
                }
            }
            indexOfLastUnsortedElement--;
        } while (swapped);
    }

    private static void startAnalytics(long startTime, long endTime) {
        long elapsedTime = (endTime - startTime);

        Runtime runtime = Runtime.getRuntime();
        long usedMemory = runtime.totalMemory() - runtime.freeMemory();

        long cpuUsage = elapsedTime * (1000000 / elapsedTime);

        System.out.println("Uso de CPU: " + cpuUsage + " nanosegundos");
        System.out.println("Memoria utilizada: " + usedMemory + " bytes");
        System.out.println("Tiempo transcurrido: " + elapsedTime + " nanosegundos");
    }
}
