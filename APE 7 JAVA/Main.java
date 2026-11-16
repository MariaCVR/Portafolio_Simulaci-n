import controlador.MonteCarloController;
import modelo.MonteCarloModel;
import vista.MonteCarloView;

public class Main {
    public static void main(String[] args) {
        int[] muestras = {1000, 10000, 100000, 1000000};

        MonteCarloModel modelo = new MonteCarloModel(42L);
        MonteCarloView vista = new MonteCarloView();
        MonteCarloController controlador = new MonteCarloController(modelo, vista);

        controlador.ejecutarExperimento(muestras, 10000);
    }
}