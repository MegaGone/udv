package TDA;

// Jimmy Martínez - Carnet No. 202302745
// Repo - https://github.com/MegaGone/udv/blob/develop/estructuras/parcial_I/TDA/Fraccion.java

public class Fraccion {
    private int numerador;
    private int denominador;

    // Constructor
    public Fraccion(int numerador, int denominador) {
        this.numerador = numerador;
        this.denominador = denominador;
    }

    // Métodos Getter y Setter
    public void setDenominador(int denominador) {
        if (denominador != 0) {
            this.denominador = denominador;
        } else {
            System.out.println("Error: El denominador debe ser distinto de cero.");
        }
    }

    public void setNumerador(int numerador) {
        this.numerador = numerador;
    }

    public int getDenominador() {
        return denominador;
    }

    public int getNumerador() {
        return numerador;
    }

    // Métodos de operaciones
    public Fraccion suma(Fraccion otraFraccion) {
        int num = (this.numerador * otraFraccion.denominador) + (otraFraccion.numerador * this.denominador);
        int den = this.denominador * otraFraccion.denominador;
        return new Fraccion(num, den);
    }

    public Fraccion resta(Fraccion otraFraccion) {
        int num = (this.numerador * otraFraccion.denominador) - (otraFraccion.numerador * this.denominador);
        int den = this.denominador * otraFraccion.denominador;
        return new Fraccion(num, den);
    }

    public Fraccion multiplicacion(Fraccion otraFraccion) {
        int num = this.numerador * otraFraccion.numerador;
        int den = this.denominador * otraFraccion.denominador;
        return new Fraccion(num, den);
    }

    public Fraccion division(Fraccion otraFraccion) {
        if (otraFraccion.numerador != 0) {
            int num = this.numerador * otraFraccion.denominador;
            int den = this.denominador * otraFraccion.numerador;
            return new Fraccion(num, den);
        } else {
            System.out.println("Error: No se puede dividir por cero.");
            return null;
        }
    }

    public Fraccion simplificacion() {
        int mcd = mcd(this.numerador, this.denominador);
        int num = this.numerador / mcd;
        int den = this.denominador / mcd;
        return new Fraccion(num, den);
    }

    public boolean esNula() {
        return this.numerador == 0;
    }

    public boolean esFraccionPropia() {
        return Math.abs(this.numerador) < Math.abs(this.denominador);
    }

    public void mostrarFraccion() {
        System.out.println(this.toString());
    }

    public void mostrarNumerador() {
        System.out.println("Numerador: " + this.numerador);
    }

    public void mostrarDenominador() {
        System.out.println("Denominador: " + this.denominador);
    }

    // Funciones de apoyo
    private int mcd(int a, int b) {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }

    @Override
    public String toString() {
        return numerador + "/" + denominador;
    }
}