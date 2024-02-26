import java.util.Scanner;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/V_quick_sort.java

public class V_quick_sort {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresar valores separados por espacios, comas o puntos: ");
        String input = scanner.nextLine();

        int[] values = handleValues(input.split("[,\\s.]+"));

        long startTime = System.nanoTime();
        quickSort(values, 0, values.length - 1);
        long endTime = System.nanoTime();

        getAnalytics(startTime, endTime);
        scanner.close();
    }

    private static int[] handleValues(String[] rawValues) {
        int[] values = new int[rawValues.length];
        for (int i = 0; i < rawValues.length; i++) {
            values[i] = Integer.parseInt(rawValues[i].trim());
        }
        return values;
    }

    private static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(array, low, high);

            quickSort(array, low, pivotIndex - 1);
            quickSort(array, pivotIndex + 1, high);
        }
    }

    private static int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (array[j] <= pivot) {
                i++;
                swap(array, i, j);
            }
        }

        swap(array, i + 1, high);
        return i + 1;
    }

    private static void swap(int[] array, int i, int j) {
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    private static void getAnalytics(long startTime, long endTime) {
        long elapsedTime = (endTime - startTime);

        Runtime runtime = Runtime.getRuntime();
        long usedMemory = runtime.totalMemory() - runtime.freeMemory();

        long cpuUsage = elapsedTime * (1000000 / elapsedTime);

        System.out.println("Uso de CPU: " + cpuUsage + " nanosegundos");
        System.out.println("Memoria utilizada: " + usedMemory + " bytes");
        System.out.println("Tiempo transcurrido: " + elapsedTime + " nanosegundos");
    }
}
