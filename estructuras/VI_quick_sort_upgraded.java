import java.util.Scanner;

public class V_quick_sort_v2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingresar valores separados por espacios, comas o puntos: ");
        String input = scanner.nextLine();

        int[] values = handleValues(input.split("[,\\s.]+"));

        long startTime = System.nanoTime();
        quickSort(values, 0, values.length - 1);
        long endTime = System.nanoTime();

        System.out.println("Array ordenado con pivote de la mediana de tres:");
        for (int num : values) {
            System.out.print(num + " ");
        }

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
        int mid = (low + high) / 2;
        int pivotIndex = findMedian(array, low, mid, high);

        int pivotValue = array[pivotIndex];
        swap(array, pivotIndex, high);

        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (array[j] <= pivotValue) {
                i++;
                swap(array, i, j);
            }
        }

        swap(array, i + 1, high);
        return i + 1;
    }

    private static int findMedian(int[] array, int low, int mid, int high) {
        if ((array[low] <= array[mid] && array[mid] <= array[high]) ||
                (array[high] <= array[mid] && array[mid] <= array[low])) {
            return mid;
        } else if ((array[mid] <= array[low] && array[low] <= array[high]) ||
                (array[high] <= array[low] && array[low] <= array[mid])) {
            return low;
        } else {
            return high;
        }
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

        System.out.println("\nUso de CPU: " + cpuUsage + " nanosegundos");
        System.out.println("Memoria utilizada: " + usedMemory + " bytes");
        System.out.println("Tiempo transcurrido: " + elapsedTime + " nanosegundos");
    }
}
