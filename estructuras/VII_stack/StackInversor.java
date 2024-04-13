import java.util.Scanner;
import java.util.Stack;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/VII_stack/
// NOTA: Ejecutar con el comando java StackInversor

public class StackInversor implements IStackInversor {

    public static void main(String[] args) {
        StackInversor stackInversor = new StackInversor();
        Integer[] list = stackInversor.requestInput();

        System.out.println("Lista Original: " + java.util.Arrays.toString(list));

        IStackInversor inverter = new StackInversor();
        inverter.invertStack(list);
        System.out.println("Lista Invertida: " + java.util.Arrays.toString(list));
    }

    // SOLICITAR 5 NUMEROS ENTEROS AL USUARIO
    private Integer[] requestInput() {
        Scanner scanner = new Scanner(System.in);
        Integer[] list = new Integer[5];

        for (int i = 0; i < 5; i++) {
            System.out.print("Ingrese el valor " + (i + 1) + ": ");
            while (!scanner.hasNextInt()) {
                System.out.println("Error: Debe ingresar un valor entero.");
                scanner.next();
                System.out.print("Ingrese el valor " + (i + 1) + ": ");
            }
            list[i] = scanner.nextInt();
        }

        scanner.close();
        return list;
    }

    @Override
    public void invertStack(Object[] elements) {
        Stack<Object> stack = new Stack<>();

        for (Object element : elements) {
            stack.push(element);
        }

        for (int i = 0; i < elements.length; i++) {
            elements[i] = stack.pop();
        }
    }
}
    