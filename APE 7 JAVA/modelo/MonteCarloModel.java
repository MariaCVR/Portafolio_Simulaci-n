package modelo;

import java.util.Random;

public class MonteCarloModel {
    private final long semilla;

    public MonteCarloModel(long semilla) {
        this.semilla = semilla;
    }

    public ResultadoSimulacion simularPi(int n, boolean guardarPuntos) {
        long inicio = System.nanoTime();

        Random rand = new Random(this.semilla);
        int nc = 0;
        double[] xs = guardarPuntos ? new double[n] : null;
        double[] ys = guardarPuntos ? new double[n] : null;
        boolean[] dentro = guardarPuntos ? new boolean[n] : null;

        for (int i = 0; i < n; i++) {
            double x = rand.nextDouble();
            double y = rand.nextDouble();
            boolean esDentro = (x * x + y * y) <= 1.0;

            if (esDentro) {
                nc++;
            }
            if (guardarPuntos) {
                xs[i] = x;
                ys[i] = y;
                dentro[i] = esDentro;
            }
        }

        double piEstimado = 4.0 * ((double) nc / n);
        double errorAbsoluto = Math.abs(Math.PI - piEstimado);

        long fin = System.nanoTime();
        double tiempoMs = (fin - inicio) / 1_000_000.0;

        return new ResultadoSimulacion(n, piEstimado, errorAbsoluto, tiempoMs, xs, ys, dentro);
    }
}