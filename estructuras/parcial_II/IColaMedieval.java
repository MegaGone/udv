package parcial_II;

public interface IColaMedieval {
    void añadir(String elemento, boolean esNoble);

    String consultarPrimero();

    void quitarPrimero();

    int consultarNumeroNobles();

    int consultarNumeroPlebeyos();

    boolean esVacia();
}
